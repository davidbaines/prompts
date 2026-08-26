#!/usr/bin/env python3
"""Validate prompt files against the library schema and run a cheap PII lint.

Run from the repo root:
    python scripts/validate.py
    python scripts/validate.py --strict   # treat warnings as errors too

Exits with code 1 if any errors are found, so it can gate a pull request in CI.
The PII lint is a heuristic, not a guarantee. It catches obvious cases so the
human reviewer can spend attention on judgement rather than proofreading.
"""

from __future__ import annotations

import argparse
import datetime
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("This script needs PyYAML. Install it with: pip install pyyaml")

PROMPTS_DIR = Path(__file__).resolve().parent.parent / "prompts"

REQUIRED_FIELDS = [
    "title", "id", "purpose", "tags", "models",
    "author", "source", "version", "created", "updated", "status",
]

ALLOWED_STATUS = {"draft", "reviewed", "proven", "deprecated"}
ALLOWED_AUTOMATION = {
    "interactive", "scheduled", "triggered", "scheduled-or-triggered",
}
KNOWN_TRIGGERS = {"cron", "email", "slack", "calendar"}

ID_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
EMAIL_PATTERN = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
LONG_DIGITS_PATTERN = re.compile(r"\d{7,}")


def split_frontmatter(text: str):
    """Return (yaml_block, body) or (None, text) if no frontmatter is present."""
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    return parts[1], parts[2]


def valid_date(value) -> bool:
    if isinstance(value, datetime.date):
        return True
    if isinstance(value, str):
        try:
            datetime.datetime.strptime(value, "%Y-%m-%d")
            return True
        except ValueError:
            return False
    return False


def is_empty(value) -> bool:
    return value in (None, "", [], {})


def check_metadata(meta: dict, path: Path):
    """Return (errors, warnings) for the frontmatter of one file."""
    errors: list[str] = []
    warnings: list[str] = []

    for field in REQUIRED_FIELDS:
        if field not in meta or is_empty(meta[field]):
            errors.append(f"missing or empty required field '{field}'")

    # id: kebab-case slug that matches the filename stem, so links stay stable.
    prompt_id = meta.get("id")
    if isinstance(prompt_id, str):
        if not ID_PATTERN.match(prompt_id):
            errors.append(f"id '{prompt_id}' is not a lowercase kebab-case slug")
        if prompt_id != path.stem:
            errors.append(
                f"id '{prompt_id}' does not match filename '{path.stem}'"
            )

    for field in ("tags", "models"):
        value = meta.get(field)
        if value is not None and not isinstance(value, list):
            errors.append(f"'{field}' must be a list, e.g. [a, b]")

    version = meta.get("version")
    if version is not None and (not isinstance(version, int) or version < 1):
        errors.append("'version' must be an integer of 1 or more")

    for field in ("created", "updated"):
        value = meta.get(field)
        if value is not None and not valid_date(value):
            errors.append(f"'{field}' must be a date in YYYY-MM-DD form")

    status = meta.get("status")
    if status is not None and status not in ALLOWED_STATUS:
        errors.append(
            f"status '{status}' is not one of {sorted(ALLOWED_STATUS)}"
        )

    # Optional automation fields, only checked when present.
    automation = meta.get("automation")
    if automation is not None and automation not in ALLOWED_AUTOMATION:
        errors.append(
            f"automation '{automation}' is not one of {sorted(ALLOWED_AUTOMATION)}"
        )

    triggers = meta.get("triggers")
    if triggers is not None and not isinstance(triggers, list):
        errors.append("'triggers' must be a list, e.g. [cron, email]")
    elif isinstance(triggers, list):
        for trg in triggers:
            if trg not in KNOWN_TRIGGERS:
                warnings.append(
                    f"trigger '{trg}' is not a known trigger "
                    f"{sorted(KNOWN_TRIGGERS)}"
                )
        if automation == "interactive" and triggers:
            warnings.append("automation is 'interactive' but triggers are listed")
        if automation in (ALLOWED_AUTOMATION - {"interactive"}) and not triggers:
            warnings.append(
                f"automation is '{automation}' but no triggers are listed"
            )

    return errors, warnings


def pii_lint(raw_text: str):
    """Cheap heuristic scan of the whole file. Returns (errors, warnings)."""
    errors: list[str] = []
    warnings: list[str] = []

    for match in EMAIL_PATTERN.findall(raw_text):
        errors.append(f"possible email address in file: '{match}'")

    for match in LONG_DIGITS_PATTERN.findall(raw_text):
        warnings.append(
            f"long digit run '{match}' (phone, ID, or figure?) worth a look"
        )

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate prompt files.")
    parser.add_argument(
        "--strict", action="store_true",
        help="treat warnings as errors (non-zero exit if any warning)",
    )
    args = parser.parse_args()

    if not PROMPTS_DIR.is_dir():
        sys.exit(f"No prompts directory found at {PROMPTS_DIR}")

    files = sorted(PROMPTS_DIR.glob("*.md"))
    if not files:
        print(f"No prompt files found in {PROMPTS_DIR}")
        return 0

    total_errors = 0
    total_warnings = 0
    clean = 0
    seen_ids: dict[str, Path] = {}

    print(f"Checking {len(files)} prompt file(s) in {PROMPTS_DIR.name}/\n")

    for path in files:
        errors: list[str] = []
        warnings: list[str] = []

        raw = path.read_text(encoding="utf-8")
        block, _ = split_frontmatter(raw)

        if block is None:
            errors.append("no YAML frontmatter block found")
        else:
            try:
                meta = yaml.safe_load(block) or {}
            except yaml.YAMLError as exc:
                meta = None
                errors.append(f"frontmatter is not valid YAML: {exc}")

            if isinstance(meta, dict):
                m_err, m_warn = check_metadata(meta, path)
                errors += m_err
                warnings += m_warn

                # Track ids to catch duplicates across files.
                pid = meta.get("id")
                if isinstance(pid, str):
                    if pid in seen_ids:
                        errors.append(
                            f"duplicate id '{pid}', also in "
                            f"{seen_ids[pid].name}"
                        )
                    else:
                        seen_ids[pid] = path
            elif meta is not None:
                errors.append("frontmatter did not parse to a mapping")

        p_err, p_warn = pii_lint(raw)
        errors += p_err
        warnings += p_warn

        if errors or warnings:
            print(path.relative_to(PROMPTS_DIR.parent))
            for e in errors:
                print(f"  ERROR: {e}")
            for w in warnings:
                print(f"  WARN:  {w}")
            print()
        else:
            clean += 1

        total_errors += len(errors)
        total_warnings += len(warnings)

    print(
        f"Summary: {len(files)} files, {clean} clean, "
        f"{total_errors} error(s), {total_warnings} warning(s)"
    )

    if total_errors > 0:
        return 1
    if args.strict and total_warnings > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
