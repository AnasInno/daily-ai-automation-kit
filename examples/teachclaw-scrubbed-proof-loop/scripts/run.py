#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED_FIELDS = {
    "workflow",
    "persona",
    "manual_workflow",
    "teacher_request",
    "class_context",
    "fake_evidence",
    "desired_artifact",
    "must_not",
    "proof_required",
}


def load_request(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    missing = sorted(REQUIRED_FIELDS - set(data))
    if missing:
        joined = ", ".join(missing)
        raise ValueError(f"Missing required field(s): {joined}")
    if not isinstance(data["fake_evidence"], list) or not data["fake_evidence"]:
        raise ValueError("fake_evidence must contain at least one item")
    return data


def build_artifact_plan(data: dict) -> list[str]:
    return [
        f"Anchor the artifact on the request: {data['teacher_request']}",
        f"Use the class context only at the safe level provided: {data['class_context']}",
        "Address each fake misconception explicitly before adding extension work.",
        f"Produce the requested artifact shape: {data['desired_artifact']}",
        "End with a human review checkpoint before claiming quality.",
    ]


def gate_rows(data: dict) -> list[tuple[str, str, str]]:
    proof = set(data["proof_required"])
    return [
        ("local code validated", "pass", "script validates required fields"),
        ("workflow mechanically validated", "pass", "sample JSON produces Markdown output"),
        (
            "output quality validated",
            "needs_judgement",
            "teacher-quality usefulness still needs human review",
        ),
        (
            "pr/ship safety validated",
            "needs_judgement" if "public-safety-scan" not in proof else "pass",
            "repo-level safety scan is separate from this example command",
        ),
    ]


def render_packet(data: dict) -> str:
    evidence = "\n".join(
        f"- {item.get('type', 'evidence')}: {item.get('detail', '').strip()}"
        for item in data["fake_evidence"]
    )
    plan = "\n".join(f"{index}. {step}" for index, step in enumerate(build_artifact_plan(data), start=1))
    gates = "\n".join(f"| {gate} | {result} | {evidence} |" for gate, result, evidence in gate_rows(data))
    boundaries = "\n".join(f"- {item}" for item in data["must_not"])
    proof = "\n".join(f"- {item}" for item in data["proof_required"])

    return "\n".join(
        [
            "# TeachClaw Scrubbed Proof Packet",
            "",
            "Status: needs_judgement",
            "Validation source of truth: local-cli, sample-output",
            "",
            "## Conversation Brief",
            "",
            f"- Workflow: {data['workflow']}",
            f"- Persona: {data['persona']}",
            f"- Manual workflow: {data['manual_workflow']}",
            f"- Teacher request: {data['teacher_request']}",
            f"- Desired artifact: {data['desired_artifact']}",
            "",
            "## Fake Evidence",
            "",
            evidence,
            "",
            "## Deterministic Artifact Plan",
            "",
            plan,
            "",
            "## Validation Gates",
            "",
            "| Gate | Result | Evidence |",
            "| --- | --- | --- |",
            gates,
            "",
            "## Required Proof",
            "",
            proof,
            "",
            "## Safety Boundaries",
            "",
            boundaries,
            "",
            "## What This Public Example Does Not Claim",
            "",
            "- live TeachClaw runtime behavior",
            "- real teacher approval",
            "- real pupil-data handling",
            "- private prompt quality",
            "- browser proof",
            "- Computer Use proof",
            "- Crabbox hydration/tool-readiness proof",
            "- Crabbox proof",
            "- autoreview/minimality verdict",
            "- CI/CD verification",
            "",
        ]
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    data = load_request(args.input)
    packet = render_packet(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(packet, encoding="utf-8")
    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
