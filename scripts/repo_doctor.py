#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    "AGENTS.md",
    ".github/workflows/check.yml",
    "README.md",
    "codex/how-i-engineer/LOAD-FIRST.md",
    "codex/how-i-engineer/KERNEL.md",
    "codex/how-i-engineer/WORKFLOW.md",
    "codex/how-i-engineer/WORK-DONE.md",
    ".agents/skills/how-i-engineer-conversation-brief/SKILL.md",
    ".agents/skills/how-i-engineer-workflow-ship/SKILL.md",
    ".agents/skills/how-i-engineer-orchestrator/SKILL.md",
    ".agents/skills/how-i-engineer-autoreview/SKILL.md",
    ".agents/skills/how-i-engineer-real-user-qa/SKILL.md",
    ".agents/skills/how-i-engineer-crabbox-proof/SKILL.md",
    ".agents/skills/how-i-engineer-eval-framework/SKILL.md",
    ".agents/skills/how-i-engineer-pr-ship-safety/SKILL.md",
    "ops/evals/README.md",
    "ops/contracts/validation-gates/README.md",
    "ops/contracts/worker-briefs/worker-brief-template.md",
    "templates/automation-brief.md",
    "examples/teachclaw-scrubbed-proof-loop/Makefile",
    "examples/teachclaw-scrubbed-eval-harness/Makefile",
    "examples/teachclaw-scrubbed-eval-harness/scripts/run_eval.py",
]


def main() -> int:
    findings: list[str] = []

    for rel in REQUIRED_PATHS:
        if not (ROOT / rel).exists():
            findings.append(f"missing required path: {rel}")

    agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    if "codex/how-i-engineer/LOAD-FIRST.md" not in agents:
        findings.append("AGENTS.md does not route to LOAD-FIRST.md")

    load_first = (ROOT / "codex/how-i-engineer/LOAD-FIRST.md").read_text(encoding="utf-8")
    for skill in sorted((ROOT / ".agents/skills").glob("*/SKILL.md")):
        text = skill.read_text(encoding="utf-8")
        rel = skill.relative_to(ROOT)
        if not text.startswith("---"):
            findings.append(f"skill missing front matter: {rel}")
        if "name:" not in text or "description:" not in text:
            findings.append(f"skill missing name/description: {rel}")
        if str(rel) not in load_first:
            findings.append(f"skill not routed from LOAD-FIRST.md: {rel}")

    if findings:
        print("REPO DOCTOR FAILED")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print("REPO DOCTOR PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
