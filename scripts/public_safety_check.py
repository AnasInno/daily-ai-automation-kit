#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


SKIP_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
}

BLOCKED_NAMES = {
    ".env",
    "cookies.txt",
}

BLOCKED_SUFFIXES = {
    ".7z",
    ".gz",
    ".har",
    ".jpeg",
    ".jpg",
    ".log",
    ".m4v",
    ".mov",
    ".mp4",
    ".pdf",
    ".png",
    ".sqlite",
    ".db",
    ".tar",
    ".webp",
    ".zip",
}

BLOCKED_PATH_MARKERS = {
    "browser-profile",
    "recording",
    "screen-recording",
    "screenshot",
    "trace",
    "traces",
}

TEXT_SUFFIXES = {
    ".bat",
    ".command",
    ".csv",
    ".json",
    ".md",
    ".py",
    ".toml",
    ".txt",
    ".yml",
    ".yaml",
}

PATTERNS = [
    ("local absolute path", re.compile(r"/Users/[A-Za-z0-9._-]+/")),
    ("OpenAI/OpenRouter style key", re.compile(r"\b(sk-[A-Za-z0-9_-]{20,}|sk-or-[A-Za-z0-9_-]{20,})\b")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z_-]{20,}\b")),
    ("GitHub token", re.compile(r"\bgh[oprsu]_[A-Za-z0-9_]{20,}\b")),
    ("private workspace marker", re.compile(r"(\.[A-Za-z0-9_-]*claw[A-Za-z0-9_-]*|docs/(private|internal|personal)(/|$)|\.(job|apply)[A-Za-z0-9_.-]*|(^|/)(inbox|mailbox|dm-export)(/|$))")),
    ("non-placeholder secret assignment", re.compile(r"(?i)(api[_-]?key|access[_-]?token|secret|password)\s*[:=]\s*['\"]?(?!$|<|your-|test-|example|placeholder|GEMINI_API_KEY)[A-Za-z0-9_.:/+=-]{12,}")),
]


def is_text(path: Path) -> bool:
    return path.suffix.lower() in TEXT_SUFFIXES or path.name in {".gitignore", "Makefile", "LICENSE", "AGENTS.md"}


def looks_like_code_plumbing(line: str) -> bool:
    return any(
        marker in line
        for marker in (
            "os.environ.get(",
            "os.getenv(",
            "api_key=args.",
            "api_key=api_key",
            "api_key.strip()",
            "GEMINI_API_KEY={",
        )
    )


def check(root: Path) -> list[str]:
    findings: list[str] = []
    for path in sorted(root.rglob("*")):
        rel = path.relative_to(root)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        if not path.is_file():
            continue
        if path.name in BLOCKED_NAMES:
            findings.append(f"blocked file: {rel}")
        if path.suffix.lower() in BLOCKED_SUFFIXES:
            findings.append(f"blocked generated/binary artifact: {rel}")
        if any(marker in part.lower() for part in rel.parts for marker in BLOCKED_PATH_MARKERS):
            findings.append(f"blocked leak-prone artifact path: {rel}")
        if not is_text(path):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            findings.append(f"non-utf8 text-like file: {rel}")
            continue
        for label, pattern in PATTERNS:
            if rel.as_posix() == "scripts/public_safety_check.py" and label == "private workspace marker":
                continue
            if label == "non-placeholder secret assignment":
                for line in text.splitlines():
                    if looks_like_code_plumbing(line):
                        continue
                    if pattern.search(line):
                        findings.append(f"{label}: {rel}")
                        break
                continue
            if pattern.search(text):
                findings.append(f"{label}: {rel}")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default=".")
    args = parser.parse_args()

    root = Path(args.path).resolve()
    findings = check(root)
    if findings:
        print("PUBLIC SAFETY CHECK FAILED")
        for finding in findings:
            print(f"- {finding}")
        return 1
    print(f"PUBLIC SAFETY CHECK PASSED: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
