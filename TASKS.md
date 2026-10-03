# Study Planner: task pool

Each task is a dictionary with `title` (nonempty string), `minutes` (nonnegative integer), and `done` (boolean). All functions preserve their inputs; functions that change records must return new dictionaries. Assume well-formed records.

All nine tasks are required for final acceptance. Each function lives in `app.py`. Inputs follow the data model above unless a task explicitly asks for validation. Return values are checked for equality; object identity matters only where new dictionaries are required. Reuse requirements are checked by peer review.

For every task: add at least one meaningful test in `tests/test_student_<ID>.py`, run the task checks, create its completion marker, and open a PR. Round two also requires a regression demonstration. Round three also requires the shared release-note edit described in `CONTRIBUTING.md`.

## S1 — Find pending tasks

Round 1 · `pending_tasks(tasks)`

Return tasks whose done value is false, preserving input order. Empty input returns `[]`.

No earlier task dependency.

Acceptance tests: `tests/test_S1.py`.

Run: `python3 check.py --task S1`; then `python3 check.py --complete S1`.

## S2 — Calculate completion percentage

Round 1 · `completion_rate(tasks)`

Return the percentage of tasks marked done, rounded with Python `round(value, 1)`. Empty input returns `0.0`. This is a count of tasks, not a percentage of minutes.

No earlier task dependency.

Acceptance tests: `tests/test_S2.py`.

Run: `python3 check.py --task S2`; then `python3 check.py --complete S2`.

## S3 — Search task titles

Round 1 · `find_tasks(tasks, query)`

Strip and casefold the query; casefold titles and use substring matching. Preserve input order. Empty or whitespace-only query returns all tasks.

No earlier task dependency.

Acceptance tests: `tests/test_S3.py`.

Run: `python3 check.py --task S3`; then `python3 check.py --complete S3`.

## S4 — Fix task completion without mutation

Round 2 · `mark_done(tasks, title)`

Return a new list of new dictionaries; set done to true for every exact title match, retaining the order and other fields. Matching an already-done task is allowed. Raise `KeyError` if no title matches. Do not modify the input, even on failure.

No earlier task dependency.

Acceptance tests: `tests/test_S4.py`.

Run: `python3 check.py --task S4`; then `python3 check.py --complete S4`.

## S5 — Fix session estimates

Round 2 · `estimate_sessions(minutes, block_minutes)`

Return the integer number of sessions needed, rounding up any partial session. Zero work requires zero sessions. Raise `ValueError` for negative minutes or block_minutes <= 0. Inputs are integers.

No earlier task dependency.

Acceptance tests: `tests/test_S5.py`.

Run: `python3 check.py --task S5`; then `python3 check.py --complete S5`.

## S6 — Fix priority ordering

Round 2 · `sort_tasks(tasks)`

Return tasks sorted by minutes descending, then casefolded title ascending. Keep original order if both keys tie. Do not sort the input in place.

No earlier task dependency.

Acceptance tests: `tests/test_S6.py`.

Run: `python3 check.py --task S6`; then `python3 check.py --complete S6`.

## S7 — Build a daily plan

Round 3 · `daily_plan(tasks, budget_minutes)`

Reuse `pending_tasks`. Scan pending tasks in their original order. Include a task when it fits the remaining budget; otherwise skip it and continue to later tasks. Return selected task records, without mutation. Raise `ValueError` for a negative integer budget. Zero-minute pending tasks can fit even a zero budget. This is a greedy scan, not an optimization problem.

Depends on: S1.

Acceptance tests: `tests/test_S7.py`.

Run: `python3 check.py --task S7`; then `python3 check.py --complete S7`.

## S8 — Build study statistics

Round 3 · `statistics(tasks)`

Reuse earlier functions. Return exactly `total_minutes` (all tasks), `pending_minutes` (unfinished tasks only), and `completion_percent` (completion_rate). Empty input returns 0, 0, and 0.0 respectively.

Depends on: S1, S2.

Acceptance tests: `tests/test_S8.py`.

Run: `python3 check.py --task S8`; then `python3 check.py --complete S8`.

## S9 — Export study tasks to CSV

Round 3 · `to_csv(tasks)`

Return CSV text with header `title,minutes,done`; encode done as 1 or 0. Preserve row order, use LF (`\n`) line endings including a final newline, and correctly quote commas, quotes and embedded newlines using `csv`. Empty input returns the header plus newline.

No earlier task dependency.

Acceptance tests: `tests/test_S9.py`.

Run: `python3 check.py --task S9`; then `python3 check.py --complete S9`.
