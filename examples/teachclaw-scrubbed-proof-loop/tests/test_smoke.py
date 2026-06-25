from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "scripts" / "run.py"
SAMPLE = ROOT / "data" / "sample_teachclaw_request.json"


def run_example(output: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(RUNNER), "--input", str(SAMPLE), "--output", str(output)],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )


def test_smoke_generates_proof_packet(tmp_path: Path) -> None:
    output = tmp_path / "proof.md"
    result = run_example(output)

    assert "Wrote" in result.stdout
    text = output.read_text(encoding="utf-8")
    assert "# TeachClaw Scrubbed Proof Packet" in text
    assert "Status: needs_judgement" in text
    assert "factorising quadratics" in text
    assert "output quality validated | needs_judgement" in text
    assert "live TeachClaw runtime behavior" in text


def test_required_fields_are_enforced(tmp_path: Path) -> None:
    broken = tmp_path / "broken.json"
    data = json.loads(SAMPLE.read_text(encoding="utf-8"))
    data.pop("teacher_request")
    broken.write_text(json.dumps(data), encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(RUNNER), "--input", str(broken), "--output", str(tmp_path / "out.md")],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "Missing required field(s): teacher_request" in result.stderr


def test_fake_evidence_must_not_be_empty(tmp_path: Path) -> None:
    broken = tmp_path / "broken.json"
    data = json.loads(SAMPLE.read_text(encoding="utf-8"))
    data["fake_evidence"] = []
    broken.write_text(json.dumps(data), encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(RUNNER), "--input", str(broken), "--output", str(tmp_path / "out.md")],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )

    assert result.returncode != 0
    assert "fake_evidence must contain at least one item" in result.stderr
