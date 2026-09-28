#!/usr/bin/env python3
"""Repository utility for SHA-256 verification.

This utility is not part of the frozen scientific analysis. It verifies either
(1) one file against an expected digest or digest text file, or
(2) a JSON manifest whose entries contain path/sha256 fields.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def expected_from_text(value: str) -> str:
    p = Path(value)
    if p.is_file():
        value = p.read_text(encoding="utf-8").strip().split()[0]
    value = value.strip().lower()
    if len(value) != 64 or any(c not in "0123456789abcdef" for c in value):
        raise ValueError("Expected digest must be a 64-character hexadecimal SHA-256 value")
    return value


def verify_single(path: Path, expected: str) -> int:
    actual = sha256_file(path)
    ok = actual == expected
    print(f"{'OK' if ok else 'FAIL'}  {path}")
    print(f"expected: {expected}")
    print(f"actual:   {actual}")
    return 0 if ok else 1


def iter_manifest_entries(obj):
    entries = obj.get("entries") if isinstance(obj, dict) else None
    if isinstance(entries, list):
        for e in entries:
            if isinstance(e, dict):
                rel = e.get("path") or e.get("file") or e.get("relative_path")
                digest = e.get("sha256") or e.get("digest")
                if rel and digest:
                    yield rel, digest
    elif isinstance(entries, dict):
        for rel, digest in entries.items():
            yield rel, digest
    elif isinstance(obj, dict):
        for rel, digest in obj.items():
            if isinstance(digest, str) and len(digest) == 64:
                yield rel, digest


def verify_manifest(manifest: Path, root: Path) -> int:
    obj = json.loads(manifest.read_text(encoding="utf-8"))
    entries = list(iter_manifest_entries(obj))
    if not entries:
        raise ValueError("No path/SHA-256 entries found in manifest")
    failures = []
    for rel, expected in entries:
        p = root / rel
        if not p.is_file():
            failures.append((rel, "missing", expected, None))
            continue
        actual = sha256_file(p)
        if actual != expected:
            failures.append((rel, "mismatch", expected, actual))
    print(f"manifest entries: {len(entries)}")
    print(f"verified: {len(entries) - len(failures)}")
    print(f"failures: {len(failures)}")
    for rel, kind, expected, actual in failures[:50]:
        print(f"FAIL [{kind}] {rel}")
        print(f"  expected: {expected}")
        if actual:
            print(f"  actual:   {actual}")
    return 0 if not failures else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    one = sub.add_parser("file", help="Verify one file")
    one.add_argument("path", type=Path)
    one.add_argument("expected", help="Digest value or path to a digest text file")
    man = sub.add_parser("manifest", help="Verify a JSON manifest")
    man.add_argument("manifest", type=Path)
    man.add_argument("--root", type=Path, default=Path("."))
    args = ap.parse_args()
    if args.cmd == "file":
        return verify_single(args.path, expected_from_text(args.expected))
    return verify_manifest(args.manifest, args.root)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2)
