# Crabbox Runs

[Crabbox](https://crabbox.sh/) is public. It is a remote testbox workflow for keeping the local developer loop simple while running proof on short-lived execution boxes.

For agent procedure, use `.agents/skills/how-i-engineer-crabbox-proof/SKILL.md`. This document is the public mental model.

The public mental model is:

```text
lease box -> hydrate tools -> sync working tree -> verify toolchain -> run command -> collect evidence -> release box
```

## How I Use It

In private project work, Crabbox is useful when I need more than a local terminal pass:

- run tests in a clean remote environment
- prove a browser or desktop path outside my normal workspace
- hydrate the box with the public tools the run needs
- verify the toolchain before trusting the proof
- collect screenshots, logs, test summaries, and run metadata
- keep evidence attached to a specific run instead of relying on memory
- release or clean up the execution environment after the proof is captured

## What This Repo Shows

This repo shows the operating habit, not the private machinery:

- use isolated runs when local proof is too weak
- treat hydration and tool readiness as part of the proof, not background noise
- separate CLI proof, browser proof, and safety proof
- keep proof artifacts inspectable
- avoid claiming a proof level that was not actually run
- publish only scrubbed docs, fake data, tests, and public-safe examples

## Hydration And Tool Readiness

A clean box only counts after it has the tools the run needs.

Public-safe hydration means:

- install or enable only the minimum runtime and tools required for the proof
- run version, doctor, or capability checks before the main command
- verify browser, MCP, CLI, or package tooling only when that tooling is part of
  the claim
- record the evidence type without publishing private configuration

For MCP or tool-bridge work, a public helper such as `mcporter` can be part of
the readiness check. The public repo can name that kind of tool and the proof
concept, but it should not publish private MCP server configs, endpoints,
tokens, project-specific tool manifests, or raw run transcripts.

## What This Repo Does Not Publish

The public artifact intentionally excludes:

- broker URLs
- provider choices for private work
- lease IDs or live runner names
- SSH details, bearer tokens, or credentials
- private hydration scripts or tool manifests
- private MCP server configs, endpoints, or tokens
- private workspace paths
- customer or user data
- private screenshots, videos, logs, or run metadata
- exact production runbooks

That keeps the repo useful as an engineering signal without turning it into an operational map.
