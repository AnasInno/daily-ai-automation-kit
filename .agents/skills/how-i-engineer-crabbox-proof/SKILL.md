---
name: how-i-engineer-crabbox-proof
description: "Use when a workflow needs isolated Crabbox command, browser, desktop, or artifact proof."
---

# Crabbox Proof

Use this skill when local proof is not enough and a run should happen in an isolated Crabbox environment.

[Crabbox](https://crabbox.sh/) is public. The safe public model is:

```text
lease box -> hydrate tools -> sync working tree -> verify toolchain -> run command -> collect evidence -> release box
```

This is for:

- proving commands away from a local laptop
- hydrating a clean box with the minimum public-safe tools needed for a proof
- checking browser or desktop paths when recorded proof matters
- verifying MCP, CLI, package, or browser tooling before trusting a run
- collecting screenshots, logs, test summaries, or run metadata
- separating proof artifacts from normal workspace noise

This is not for:

- publishing broker URLs
- publishing provider choices for private work
- publishing lease IDs, SSH details, bearer tokens, screenshots, videos, private logs, or live run metadata
- publishing private hydration scripts, MCP configs, tool manifests, endpoints, or raw transcripts
- treating Crabbox mechanics as output-quality proof

## Public-Safe Flow

1. Check whether Crabbox is available.
2. Hydrate the box with the minimum runtime and public-safe tools needed.
3. Verify the toolchain with version, doctor, or capability checks.
4. Run the smallest useful command in Crabbox.
5. Collect or note the evidence type.
6. Classify the proof: command, browser, desktop, artifact, or mechanics.
7. Release or clean up the run.
8. Record only public-safe proof notes.

For MCP or tool-bridge proof, a public helper such as `mcporter` may be checked
as part of tool readiness. Do not publish private MCP server configs, endpoints,
tokens, project-specific manifests, or raw transcripts.

## Generic Commands

Use commands like these only when configured safely:

```bash
crabbox doctor
crabbox run -- tool-name --version
crabbox run -- make check
crabbox artifacts collect
```

If Crabbox is not installed or configured, fall back to local proof and report:

```text
Crabbox proof not run; local proof only.
```

## Output Standard

Report:

- command attempted
- hydration/tool checks performed
- proof surface
- whether it passed
- public-safe artifact summary
- cleanup state
- what Crabbox did not prove

Never include private broker URLs, provider choices, lease IDs, tokens, SSH hosts, screenshots with sensitive data, or exact private evidence paths.
