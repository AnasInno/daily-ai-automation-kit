# Verify

## Commands

```bash
make smoke
python3 -m pytest -q
```

## Expected Result

- `output/sample_proof_packet.md` is generated
- tests pass
- no secrets or private details are required

## Proof Status

- `mechanical_result`: `pass`
- `quality_result`: `needs_judgement`
- `validation_source_of_truth`: `local-cli`, `unit-tests`, `sample-output`

This public example proves the workflow mechanics. It does not claim real TeachClaw runtime, browser, Crabbox, or teacher-quality validation.
It also does not claim Computer Use proof, Crabbox hydration/tool-readiness
proof, an autoreview/minimality verdict, or CI/CD verification.
