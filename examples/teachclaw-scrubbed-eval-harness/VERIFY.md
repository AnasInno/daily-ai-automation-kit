# Verify

## Commands

```bash
make smoke
python3 -m pytest -q
```

## Expected Result

- `output/eval_scorecard.json` is generated
- `output/eval_scorecard.md` is generated
- tests pass
- no secrets or private details are required

## Proof Status

- `mechanical_result`: `pass`
- `quality_result`: `pass_fixture`
- `validation_source_of_truth`: `fixture-rubric`, `deterministic-scorer`, `sample-output`

This public example proves eval mechanics. It does not claim live TeachClaw
runtime, live model quality, browser, Computer Use, Crabbox, Crabbox
hydration/tool readiness, autoreview/minimality, CI/CD verification, or real
teacher validation.
