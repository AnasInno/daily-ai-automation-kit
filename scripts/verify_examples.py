#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = [
    ROOT / "examples" / "teachclaw-scrubbed-proof-loop",
    ROOT / "examples" / "teachclaw-scrubbed-eval-harness",
]


def run(cmd: list[str], cwd: Path) -> None:
    print(f"$ {' '.join(cmd)}  # cwd={cwd.relative_to(ROOT)}")
    subprocess.run(cmd, cwd=cwd, check=True, text=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()

    if not args.smoke and not args.test:
        args.smoke = True
        args.test = True

    for example in EXAMPLES:
        if args.smoke:
            run(["make", "smoke"], example)
        if args.test:
            run([sys.executable, "-m", "pytest", "-q"], example)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
