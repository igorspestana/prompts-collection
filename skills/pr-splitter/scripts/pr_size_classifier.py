#!/usr/bin/env python3
import argparse
import subprocess
import sys


def run_git_numstat(base_ref: str, head_ref: str) -> str:
    result = subprocess.run(
        ["git", "diff", "--numstat", f"{base_ref}...{head_ref}"],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        sys.stderr.write(result.stderr)
        raise SystemExit(result.returncode)
    return result.stdout


def classify(total_lines: int) -> str:
    if total_lines <= 50:
        return "PP"
    if total_lines <= 200:
        return "P"
    if total_lines <= 500:
        return "M"
    if total_lines <= 1000:
        return "G"
    return "GG"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Classify a PR/branch diff by changed lines."
    )
    parser.add_argument("base_ref")
    parser.add_argument("head_ref")
    args = parser.parse_args()

    output = run_git_numstat(args.base_ref, args.head_ref)

    files_changed = 0
    insertions = 0
    deletions = 0

    for line in output.splitlines():
        if not line.strip():
            continue
        parts = line.split("\t", 2)
        if len(parts) < 3:
            continue
        added, removed, _path = parts
        files_changed += 1
        if added.isdigit():
            insertions += int(added)
        if removed.isdigit():
            deletions += int(removed)

    total_lines = insertions + deletions
    size_class = classify(total_lines)

    print(f"base_ref: {args.base_ref}")
    print(f"head_ref: {args.head_ref}")
    print(f"files_changed: {files_changed}")
    print(f"insertions: {insertions}")
    print(f"deletions: {deletions}")
    print(f"total_lines: {total_lines}")
    print(f"classification: {size_class}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
