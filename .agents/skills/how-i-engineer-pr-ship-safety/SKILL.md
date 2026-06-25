---
name: how-i-engineer-pr-ship-safety
description: "Use before submitting a PR, merging, shipping, or presenting this repo or a generated workflow artifact."
---

# PR / Ship Safety

Use this skill before PR-shaped, merge-shaped, or ship-shaped actions.

This is for:

- checking whether the repo is safe to submit, merge, or present
- verifying docs match commands
- scanning for secrets and private details
- confirming proof claims are honest
- preparing a merge/ship verdict

This is not for:

- pushing or submitting PRs without user approval
- hiding failed proof
- shipping generated archives without inspection

## Required Checks

From repo root:

```bash
make check
git status --short
```

For PR/ship flows, also verify that CI/CD runs the same proof chain when
available:

```bash
make check
# CI/CD should run the equivalent command on push or pull request.
```

Also inspect:

- `README.md`
- `AGENTS.md`
- `docs/what-not-to-publish.md`
- generated sample outputs
- `.env.example` files
- any new archives, databases, browser files, screenshots, or logs

## Claim Audit

For each public claim, name the proof:

- CLI smoke
- unit tests
- output inspection
- browser proof
- computer proof
- Crabbox proof
- Crabbox hydration/tool-readiness proof
- autoreview/minimality verdict
- safety scan
- human judgement
- CI/CD check

If a proof was not run, say so.

## Blockers

Stop release if you find:

- real API keys or `.env` files
- local absolute paths
- customer data
- inbox or browser profile material
- private screenshots or logs
- Crabbox broker URLs, lease IDs, tokens, or private run evidence
- private hydration scripts, MCP configs, tool manifests, or raw transcripts
- claimed browser, computer, Crabbox, or tool-readiness proof without recorded evidence
- generated zip/database artifacts not intentionally released
- README commands that do not work
- CI/CD is red or not configured for a claimed CI/CD proof

## Verdict

Return one:

- `fail`
- `needs repair`
- `needs judgement`
- `merge candidate`

Do not use `merge candidate` if the public claim depends on a proof surface that
was not run.
