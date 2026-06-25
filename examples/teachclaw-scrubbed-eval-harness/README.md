# TeachClaw Scrubbed Eval Harness

This is a public-safe version of the eval spine behind TeachClaw-shaped work.

It does not contain TeachClaw private source, prompts, live traces, pupil work,
teacher data, browser sessions, Crabbox metadata, provider keys, or production
run logs.

It shows the loop:

```text
fake scenario pack -> candidate strategies -> weighted rubric -> deterministic scorecard -> proof boundary
```

## Run

```bash
make smoke
```

This reads fake scenarios, fake candidate strategy scores, and a public rubric.
It writes:

- `output/eval_scorecard.json`
- `output/eval_scorecard.md`

## Test

```bash
python3 -m pytest -q
```

## What This Proves

- the repo has a runnable eval harness, not just eval language
- quality gates are separate from smoke tests
- strategy comparison is visible by scenario and by task family
- public-safe fixtures can show the shape of serious eval work
- fixture-only proof is labelled honestly

## What This Does Not Prove

- live TeachClaw model quality
- private prompt quality
- real teacher approval
- real pupil-data handling
- browser proof
- Computer Use proof
- Crabbox hydration/tool-readiness proof
- Crabbox proof
- autoreview/minimality verdict
- CI/CD verification
- production routing decisions

Those require recorded private evidence and stay out of this public example.
