#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_rubric(rubric: dict[str, Any]) -> list[dict[str, Any]]:
    required = {"rubric_version", "scale", "release_threshold", "needs_repair_below", "dimensions"}
    missing = sorted(required - set(rubric))
    if missing:
        raise ValueError(f"Rubric missing required field(s): {', '.join(missing)}")

    dimensions = rubric["dimensions"]
    if not isinstance(dimensions, list) or not dimensions:
        raise ValueError("Rubric dimensions must be a non-empty list")

    ids = [item["id"] for item in dimensions]
    if len(ids) != len(set(ids)):
        raise ValueError("Rubric dimension ids must be unique")

    total_weight = sum(float(item["weight"]) for item in dimensions)
    if abs(total_weight - 1.0) > 0.0001:
        raise ValueError(f"Rubric weights must sum to 1.0, got {total_weight:.4f}")

    return dimensions


def validate_scenarios(pack: dict[str, Any]) -> dict[str, dict[str, Any]]:
    required = {"pack_id", "scenarios"}
    missing = sorted(required - set(pack))
    if missing:
        raise ValueError(f"Scenario pack missing required field(s): {', '.join(missing)}")

    scenarios = pack["scenarios"]
    if not isinstance(scenarios, list) or not scenarios:
        raise ValueError("Scenario pack must contain at least one scenario")

    by_id = {item["id"]: item for item in scenarios}
    if len(by_id) != len(scenarios):
        raise ValueError("Scenario ids must be unique")
    return by_id


def validate_runs(
    runs: dict[str, Any],
    scenarios: dict[str, dict[str, Any]],
    dimension_ids: set[str],
    scale_min: int,
    scale_max: int,
) -> dict[str, dict[str, Any]]:
    required = {"run_id", "eval_version", "validation_source_of_truth", "strategies", "scores", "non_claims"}
    missing = sorted(required - set(runs))
    if missing:
        raise ValueError(f"Run fixture missing required field(s): {', '.join(missing)}")

    strategies = {item["id"]: item for item in runs["strategies"]}
    if len(strategies) != len(runs["strategies"]):
        raise ValueError("Strategy ids must be unique")

    seen_pairs: set[tuple[str, str]] = set()
    for score in runs["scores"]:
        scenario_id = score["scenario_id"]
        strategy_id = score["strategy_id"]
        if scenario_id not in scenarios:
            raise ValueError(f"Unknown scenario id in score: {scenario_id}")
        if strategy_id not in strategies:
            raise ValueError(f"Unknown strategy id in score: {strategy_id}")

        pair = (scenario_id, strategy_id)
        if pair in seen_pairs:
            raise ValueError(f"Duplicate score for scenario/strategy: {scenario_id}/{strategy_id}")
        seen_pairs.add(pair)

        scores = score["dimension_scores"]
        found_dimensions = set(scores)
        if found_dimensions != dimension_ids:
            missing_dimensions = sorted(dimension_ids - found_dimensions)
            extra_dimensions = sorted(found_dimensions - dimension_ids)
            details = []
            if missing_dimensions:
                details.append(f"missing {', '.join(missing_dimensions)}")
            if extra_dimensions:
                details.append(f"extra {', '.join(extra_dimensions)}")
            raise ValueError(f"Invalid dimensions for {scenario_id}/{strategy_id}: {'; '.join(details)}")

        for dimension_id, value in scores.items():
            if not isinstance(value, int) or value < scale_min or value > scale_max:
                raise ValueError(
                    f"Score for {scenario_id}/{strategy_id}/{dimension_id} must be an integer from {scale_min} to {scale_max}"
                )

    expected_pairs = {(scenario_id, strategy_id) for scenario_id in scenarios for strategy_id in strategies}
    missing_pairs = sorted(expected_pairs - seen_pairs)
    if missing_pairs:
        readable = ", ".join(f"{scenario}/{strategy}" for scenario, strategy in missing_pairs)
        raise ValueError(f"Missing score fixture(s): {readable}")

    return strategies


def score_status(
    weighted_score: float,
    failed_dimensions: list[str],
    fatal_failures: list[str],
    precheck_failures: list[str],
    merge_threshold: float,
    needs_repair_below: float,
) -> str:
    if fatal_failures:
        return "fail"
    if precheck_failures or weighted_score < needs_repair_below:
        return "needs_repair"
    if failed_dimensions or weighted_score < merge_threshold:
        return "needs_judgement"
    return "merge_candidate"


def evaluate_score(
    raw_score: dict[str, Any],
    scenario: dict[str, Any],
    strategy: dict[str, Any],
    dimensions: list[dict[str, Any]],
    merge_threshold: float,
    needs_repair_below: float,
) -> dict[str, Any]:
    dimension_scores = raw_score["dimension_scores"]
    weighted_score = round(
        sum(float(dimension["weight"]) * dimension_scores[dimension["id"]] for dimension in dimensions),
        2,
    )
    failed_dimensions = [
        dimension["id"]
        for dimension in dimensions
        if dimension_scores[dimension["id"]] < int(dimension["pass_at"])
    ]
    fatal_failures = [
        dimension["id"]
        for dimension in dimensions
        if "fatal_below" in dimension and dimension_scores[dimension["id"]] < int(dimension["fatal_below"])
    ]
    precheck_failures = raw_score.get("precheck_failures", [])
    status = score_status(
        weighted_score,
        failed_dimensions,
        fatal_failures,
        precheck_failures,
        merge_threshold,
        needs_repair_below,
    )
    status_reasons = []
    status_reasons.extend(f"fatal: {item}" for item in fatal_failures)
    status_reasons.extend(precheck_failures)
    status_reasons.extend(f"below pass: {item}" for item in failed_dimensions)
    if weighted_score < merge_threshold and not status_reasons:
        status_reasons.append("below merge threshold")
    if not status_reasons:
        status_reasons.append("none")

    return {
        "scenario_id": raw_score["scenario_id"],
        "family": scenario["family"],
        "mode": scenario["mode"],
        "strategy_id": raw_score["strategy_id"],
        "strategy_label": strategy["label"],
        "weighted_score": weighted_score,
        "status": status,
        "failed_dimensions": failed_dimensions,
        "fatal_failures": fatal_failures,
        "precheck_failures": precheck_failures,
        "status_reasons": status_reasons,
        "latency_ms": raw_score["latency_ms"],
        "estimated_cost_units": raw_score["estimated_cost_units"],
        "judge_notes": raw_score.get("judge_notes", []),
    }


def summarize_strategies(results: list[dict[str, Any]], strategies: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for result in results:
        grouped[result["strategy_id"]].append(result)

    summaries = []
    for strategy_id, rows in sorted(grouped.items()):
        statuses = [row["status"] for row in rows]
        fail_count = statuses.count("fail")
        needs_repair_count = statuses.count("needs_repair")
        needs_judgement_count = statuses.count("needs_judgement")
        merge_candidate_count = statuses.count("merge_candidate")

        if fail_count:
            routing_verdict = "not_ready"
        elif needs_repair_count:
            routing_verdict = "needs_repair"
        elif needs_judgement_count:
            routing_verdict = "recommended_with_review_gate"
        else:
            routing_verdict = "merge_candidate"

        summaries.append(
            {
                "strategy_id": strategy_id,
                "label": strategies[strategy_id]["label"],
                "role": strategies[strategy_id]["role"],
                "average_score": round(sum(row["weighted_score"] for row in rows) / len(rows), 2),
                "merge_candidate_count": merge_candidate_count,
                "needs_judgement_count": needs_judgement_count,
                "needs_repair_count": needs_repair_count,
                "fail_count": fail_count,
                "average_latency_ms": round(sum(row["latency_ms"] for row in rows) / len(rows)),
                "total_cost_units": round(sum(row["estimated_cost_units"] for row in rows), 2),
                "routing_verdict": routing_verdict,
            }
        )
    return summaries


def compare_pairwise(results: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for result in results:
        grouped[result["scenario_id"]].append(result)

    comparisons = []
    for scenario_id, rows in sorted(grouped.items()):
        ordered = sorted(rows, key=lambda item: (item["weighted_score"], item["status"]), reverse=True)
        winner = ordered[0]
        runner_up = ordered[1] if len(ordered) > 1 else None
        comparisons.append(
            {
                "scenario_id": scenario_id,
                "winner_strategy_id": winner["strategy_id"],
                "winner_score": winner["weighted_score"],
                "runner_up_strategy_id": runner_up["strategy_id"] if runner_up else None,
                "score_delta": round(winner["weighted_score"] - runner_up["weighted_score"], 2) if runner_up else None,
            }
        )
    return comparisons


def select_recommendation(summaries: list[dict[str, Any]]) -> dict[str, Any]:
    ranked = sorted(
        summaries,
        key=lambda item: (
            item["fail_count"] == 0,
            item["needs_repair_count"] == 0,
            item["average_score"],
            -item["total_cost_units"],
        ),
        reverse=True,
    )
    winner = ranked[0]
    return {
        "strategy_id": winner["strategy_id"],
        "label": winner["label"],
        "routing_verdict": winner["routing_verdict"],
        "reason": "highest fixture score without fatal failures; review gate remains where scenario risk requires it",
    }


def build_scorecard(pack: dict[str, Any], rubric: dict[str, Any], runs: dict[str, Any]) -> dict[str, Any]:
    dimensions = validate_rubric(rubric)
    scenarios = validate_scenarios(pack)
    dimension_ids = {dimension["id"] for dimension in dimensions}
    strategies = validate_runs(
        runs,
        scenarios,
        dimension_ids,
        int(rubric["scale"]["min"]),
        int(rubric["scale"]["max"]),
    )

    scenario_results = [
        evaluate_score(
            raw_score,
            scenarios[raw_score["scenario_id"]],
            strategies[raw_score["strategy_id"]],
            dimensions,
            float(rubric["release_threshold"]),
            float(rubric["needs_repair_below"]),
        )
        for raw_score in runs["scores"]
    ]
    strategy_summaries = summarize_strategies(scenario_results, strategies)
    pairwise = compare_pairwise(scenario_results)
    recommendation = select_recommendation(strategy_summaries)

    return {
        "eval_version": runs["eval_version"],
        "run_id": runs["run_id"],
        "pack_id": pack["pack_id"],
        "rubric_version": rubric["rubric_version"],
        "validation_source_of_truth": runs["validation_source_of_truth"],
        "mechanical_result": "pass",
        "quality_result": "pass_fixture",
        "overall_status": "needs_judgement",
        "recommendation": recommendation,
        "strategy_summaries": strategy_summaries,
        "pairwise_comparisons": pairwise,
        "scenario_results": scenario_results,
        "non_claims": runs["non_claims"],
    }


def render_markdown(scorecard: dict[str, Any]) -> str:
    strategy_rows = [
        "| Strategy | Avg score | Merge | Review | Repair | Fail | Avg latency | Cost | Verdict |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |",
    ]
    for item in scorecard["strategy_summaries"]:
        strategy_rows.append(
            "| {label} | {average_score:.2f} | {merge_candidate_count} | {needs_judgement_count} | "
            "{needs_repair_count} | {fail_count} | {average_latency_ms}ms | {total_cost_units:.2f} | {routing_verdict} |".format(
                **item
            )
        )

    scenario_rows = [
        "| Scenario | Family | Strategy | Score | Status | Status reason |",
        "| --- | --- | --- | ---: | --- | --- |",
    ]
    for item in scorecard["scenario_results"]:
        scenario_rows.append(
            f"| {item['scenario_id']} | {item['family']} | {item['strategy_label']} | "
            f"{item['weighted_score']:.2f} | {item['status']} | {format_status_reasons(item['status_reasons'])} |"
        )

    pairwise_rows = [
        "| Scenario | Winner | Delta |",
        "| --- | --- | ---: |",
    ]
    for item in scorecard["pairwise_comparisons"]:
        pairwise_rows.append(
            f"| {item['scenario_id']} | {item['winner_strategy_id']} | {item['score_delta']:.2f} |"
        )

    non_claims = "\n".join(f"- {item}" for item in scorecard["non_claims"])
    sources = ", ".join(scorecard["validation_source_of_truth"])
    rec = scorecard["recommendation"]

    return "\n".join(
        [
            "# TeachClaw Scrubbed Eval Scorecard",
            "",
            f"Run: {scorecard['run_id']}",
            f"Status: {scorecard['overall_status']}",
            f"Validation source of truth: {sources}",
            "",
            "## Recommendation",
            "",
            f"- Strategy: {rec['label']}",
            f"- Verdict: {rec['routing_verdict']}",
            f"- Reason: {rec['reason']}",
            "",
            "## Strategy Summary",
            "",
            *strategy_rows,
            "",
            "## Scenario Results",
            "",
            *scenario_rows,
            "",
            "## Pairwise Winners",
            "",
            *pairwise_rows,
            "",
            "## What This Public Eval Does Not Claim",
            "",
            non_claims,
            "",
        ]
    )


def format_status_reasons(reasons: list[str]) -> str:
    if reasons == ["none"]:
        return "none"

    dimension_gaps = [item.removeprefix("below pass: ") for item in reasons if item.startswith("below pass: ")]
    direct_reasons = [item for item in reasons if not item.startswith("below pass: ")]

    parts = direct_reasons[:]
    if dimension_gaps:
        shown = ", ".join(dimension_gaps[:3])
        hidden_count = len(dimension_gaps) - 3
        suffix = f" +{hidden_count} more" if hidden_count > 0 else ""
        parts.append(f"dimension gaps: {shown}{suffix}")

    return "; ".join(parts)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scenarios", required=True, type=Path)
    parser.add_argument("--rubric", required=True, type=Path)
    parser.add_argument("--runs", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()

    scorecard = build_scorecard(
        read_json(args.scenarios),
        read_json(args.rubric),
        read_json(args.runs),
    )

    args.output_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.output_dir / "eval_scorecard.json"
    md_path = args.output_dir / "eval_scorecard.md"
    json_path.write_text(json.dumps(scorecard, indent=2) + "\n", encoding="utf-8")
    md_path.write_text(render_markdown(scorecard), encoding="utf-8")
    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
