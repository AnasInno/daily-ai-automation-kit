from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "scripts" / "run_eval.py"
SCENARIOS = ROOT / "data" / "scenarios.json"
RUBRIC = ROOT / "data" / "rubric.json"
RUNS = ROOT / "data" / "candidate_runs.json"


def run_eval(output_dir: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(RUNNER),
            "--scenarios",
            str(SCENARIOS),
            "--rubric",
            str(RUBRIC),
            "--runs",
            str(RUNS),
            "--output-dir",
            str(output_dir),
        ],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )


def test_smoke_generates_scorecards(tmp_path: Path) -> None:
    result = run_eval(tmp_path)

    assert "eval_scorecard.json" in result.stdout
    scorecard = json.loads((tmp_path / "eval_scorecard.json").read_text(encoding="utf-8"))
    markdown = (tmp_path / "eval_scorecard.md").read_text(encoding="utf-8")

    assert scorecard["mechanical_result"] == "pass"
    assert scorecard["quality_result"] == "pass_fixture"
    assert scorecard["overall_status"] == "needs_judgement"
    assert scorecard["recommendation"]["strategy_id"] == "agentic_checked"
    assert "Strategy Summary" in markdown
    assert "What This Public Eval Does Not Claim" in markdown


def test_agentic_strategy_wins_each_pairwise_case(tmp_path: Path) -> None:
    run_eval(tmp_path)
    scorecard = json.loads((tmp_path / "eval_scorecard.json").read_text(encoding="utf-8"))

    winners = {item["winner_strategy_id"] for item in scorecard["pairwise_comparisons"]}
    assert winners == {"agentic_checked"}
    assert all(item["score_delta"] > 0 for item in scorecard["pairwise_comparisons"])


def test_invalid_dimension_is_rejected(tmp_path: Path) -> None:
    broken_runs = tmp_path / "broken_runs.json"
    data = json.loads(RUNS.read_text(encoding="utf-8"))
    data["scores"][0]["dimension_scores"].pop("task_completion")
    broken_runs.write_text(json.dumps(data), encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            str(RUNNER),
            "--scenarios",
            str(SCENARIOS),
            "--rubric",
            str(RUBRIC),
            "--runs",
            str(broken_runs),
            "--output-dir",
            str(tmp_path / "out"),
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "Invalid dimensions" in result.stderr
    assert "task_completion" in result.stderr


def test_rubric_weights_are_enforced(tmp_path: Path) -> None:
    broken_rubric = tmp_path / "broken_rubric.json"
    data = json.loads(RUBRIC.read_text(encoding="utf-8"))
    data["dimensions"][0]["weight"] = 0.99
    broken_rubric.write_text(json.dumps(data), encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            str(RUNNER),
            "--scenarios",
            str(SCENARIOS),
            "--rubric",
            str(broken_rubric),
            "--runs",
            str(RUNS),
            "--output-dir",
            str(tmp_path / "out"),
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "Rubric weights must sum to 1.0" in result.stderr
