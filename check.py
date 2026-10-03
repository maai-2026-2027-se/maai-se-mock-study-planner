#!/usr/bin/env python3
"""Run baseline, completed-task, candidate-task, or final acceptance checks."""
import argparse
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--task", help="Also test this candidate task without changing files")
    mode.add_argument("--complete", help="Test this task and write its completion marker on success")
    mode.add_argument("--all", action="store_true", help="Require every task and release criterion")
    args = parser.parse_args()
    tasks = json.loads((ROOT / "tasks.json").read_text())
    ids = {task["id"] for task in tasks}
    candidate = args.task or args.complete
    if candidate and candidate not in ids:
        parser.error(f"Unknown task {candidate!r}. Choose from {', '.join(sorted(ids))}.")
    completed = set()
    errors = []
    for marker in sorted((ROOT / "completed").iterdir()):
        if marker.name == ".gitkeep":
            continue
        if not marker.is_file() or marker.suffix != ".txt" or marker.stem not in ids:
            errors.append(f"Unknown completion marker: {marker.name}")
        elif marker.read_text().strip() != marker.stem:
            errors.append(f"Marker {marker.name} must contain only {marker.stem}.")
        else:
            completed.add(marker.stem)
    selected = ids if args.all else completed | ({candidate} if candidate else set())
    if args.all and completed != ids:
        errors.append("Missing completion markers: " + ", ".join(sorted(ids - completed)))
    release_required = ids if args.all else completed | ({args.complete} if args.complete else set())
    round_three = {task["id"] for task in tasks if task["round"] == 3} & release_required
    if round_three:
        lines = (ROOT / "RELEASE_NOTES.md").read_text().splitlines()
        release_lines = [line for line in lines if line.startswith("Round 3 features: ")]
        released = set()
        if len(release_lines) == 1:
            released = {part.strip() for part in release_lines[0].removeprefix("Round 3 features: ").removesuffix(".").split(",")}
        if not round_three <= released:
            errors.append("Keep one 'Round 3 features: ...' line containing: " + ", ".join(sorted(round_three)))
        if any(line.startswith(("<<<<<<<", "=======", ">>>>>>>")) for line in lines):
            errors.append("RELEASE_NOTES.md still contains merge conflict markers.")
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromName("tests.test_baseline"))
    for task_id in sorted(selected):
        suite.addTests(loader.loadTestsFromName(f"tests.test_{task_id}"))
    for file in sorted((ROOT / "tests").glob("test_student_*.py")):
        suite.addTests(loader.loadTestsFromName(f"tests.{file.stem}"))
    print(f"Checking baseline + {len(selected)}/{len(ids)} task suites + student tests", flush=True)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    for error in errors:
        print(f"RELEASE ERROR: {error}", file=sys.stderr)
    if not result.wasSuccessful() or errors:
        return 1
    if args.complete:
        marker = ROOT / "completed" / f"{args.complete}.txt"
        marker.write_text(args.complete + "\n")
        print(f"Passed. Commit {marker.relative_to(ROOT)} with the implementation.")
    elif args.all:
        print("FINAL ACCEPTANCE PASSED: all tasks, markers and release notes verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
