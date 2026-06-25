# Worker Brief

## Identity

- worker type:
- assigned by:
- date:

## Task

- task id:
- goal:
- lane: `conversation` | `research` | `build` | `eval` | `autoreview` | `QA` | `browser` | `computer` | `Crabbox` | `release`
- why this matters now:

## Scope

- allowed files:
- forbidden files:
- expected deliverable:
- external actions allowed: `none` unless explicitly approved

## Workflow

- user/persona:
- current manual workflow:
- input:
- output:
- deterministic core:
- optional AI layer:
- safety boundaries:

## Validation

- focused commands:
- sample input:
- expected output:
- required validation source:
- visible tool required: `none` | `Browser Use` | `Computer Use`
- browser proof required: `yes` | `no`
- computer proof required: `yes` | `no`
- Crabbox proof required: `yes` | `no`
- tool-readiness proof required: `yes` | `no`
- autoreview required: `yes` | `no`
- human judgement required: `yes` | `no`

## Constraints

- follow `AGENTS.md` and `codex/how-i-engineer/LOAD-FIRST.md`
- keep the slice scoped
- no real customer data
- no secrets, `.env`, browser profiles, inboxes, private logs, or local absolute paths
- no external writes without explicit approval
- do not claim browser, computer, or Crabbox proof unless recorded

## Return Format

- changed files:
- commands run:
- output produced:
- validation source of truth:
- mechanical result:
- quality result:
- blockers:
- what was not proved:
- suggested next validation step:
