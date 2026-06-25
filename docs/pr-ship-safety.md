# PR / Ship Safety Gate

Public-safe engineering repos need a stricter bar than local prototypes. The
PR/ship gate is where the agentic system proves it can ship without leaking the
workshop.

For agent procedure, use `.agents/skills/how-i-engineer-pr-ship-safety/SKILL.md`. This document explains the standard.

## Do Publish

- fake sample data
- deterministic demo paths
- small scripts with clear inputs and outputs
- public-source adapters when they are safe
- `.env.example` with placeholder names only
- tests and smoke proof
- eval scorecards when output quality or routing is part of the claim
- clear limitations

## Do Publish As Proof

- the brief
- the deterministic command
- the test command
- a fake sample output
- a fixture scorecard when public eval mechanics are being shown
- a Crabbox run note when isolated remote proof was actually used
- a browser E2E note when a browser run was actually recorded
- a Computer Use note when a desktop or OS-level visual run was actually recorded
- an autoreview/minimality note for non-trivial changes
- a CI/CD note for PR or merge checks
- a safety scan command

## Do Not Publish

- real API keys
- `.env` files
- local absolute paths
- customer records
- inbox exports
- DMs or screenshots with personal details
- browser profiles, cookies, or session data
- Crabbox broker URLs, lease IDs, provider choices, SSH details, or auth tokens
- private hydration scripts, MCP configs, tool manifests, endpoints, or raw transcripts
- private agent instructions or scratchpads
- generated release zips by accident
- old experimental git history

## External Actions

Examples should not send email, write to CRMs, post online, or update live systems by default.

If an example ever supports an external write, it should require an explicit flag and a dry-run mode.

## Merge Candidate Checklist

- `make check` passes
- CI/CD is configured for push or pull request
- generated junk is removed or ignored
- `.env.example` contains placeholders only
- sample data is fake or public-safe
- output files are intentional
- git history is clean
- README commands match reality
- claims are specific about CLI proof, eval proof, browser proof, computer
  proof, Crabbox proof, tool-readiness proof, autoreview, CI/CD proof, and
  safety proof
