---
name: how-i-engineer-eval-framework
description: "Use when designing, running, or reviewing a public-safe eval harness for an AI-assisted workflow."
---

# Eval Framework

Use this skill when the work changes model behavior, generated output quality,
routing decisions, confidence thresholds, or public claims about usefulness.

This is for:

- scenario packs
- rubric design
- deterministic prechecks
- fixture or live-output scorecards
- pairwise strategy comparison
- quality gates that stay separate from smoke tests

This is not for:

- treating one nice output as proof
- publishing private prompts, private run logs, pupil data, customer data, or live model traces
- claiming live model quality from fixture-only runs
- replacing human judgement where the workflow requires it

## Required Context

Load:

- `ops/evals/README.md`
- `docs/eval-framework.md`
- `ops/contracts/validation-gates/README.md`

Load the example at `examples/teachclaw-scrubbed-eval-harness/` when you need a runnable pattern.

## Eval Loop

1. Define the task family and user-facing outcome.
2. Build a small scenario pack with gold, edge, and failure-mode cases.
3. Define a rubric with weighted dimensions and fatal safety gates.
4. Add deterministic prechecks for required sections, file shape, or forbidden actions.
5. Score candidate outputs or strategies against the rubric.
6. Compare strategies by task family, not by one blended average.
7. Record cost, latency, variance, and judge notes when available.
8. Emit JSON for machines and Markdown for humans.
9. Label proof honestly: fixture, local, browser, computer, Crabbox, live, or human-review.
10. Keep release verdicts separate from eval mechanics.

## Output Standard

Return:

- scenario pack used
- rubric version
- candidates or strategies compared
- deterministic prechecks
- scorecard path
- winning strategy, if any
- quality result
- proof source of truth
- what this eval did not prove

If the run uses fake fixtures, say so directly.
