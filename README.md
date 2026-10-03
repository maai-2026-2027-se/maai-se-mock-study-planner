# Study Planner

Organize study tasks, estimate work sessions, and build a small daily plan.

This is a three-round team exercise. Start with [the student guide](CONTRIBUTING.md), then read your assigned card in [TASKS.md](TASKS.md). Your instructor supplies the author/reviewer schedule.

## Run it

Use Python 3.11 or later. No third-party packages are required.

```sh
python3 app.py
python3 check.py
```

The demo prints sample records and the existing `total_minutes` result. Extend the Python functions according to the task cards. The starter has intentionally missing features and round-two bugs; baseline checks pass but final acceptance fails until the team finishes.

## Data model

Each task is a dictionary with `title` (nonempty string), `minutes` (nonnegative integer), and `done` (boolean). All functions preserve their inputs; functions that change records must return new dictionaries. Assume well-formed records.

## Test a task

```sh
python3 check.py --task S1
# After implementation and a meaningful student test:
python3 check.py --complete S1
```

Commit `completed/S1.txt` with your code and test. Normal CI checks the baseline, every completed task, and student tests. Do not edit the supplied acceptance tests, runner, task manifest, or workflow.

After all rounds, run `python3 check.py --all` on current `main`. All nine tasks must pass, all nine markers must exist, and the shared release-note line must contain S7, S8 and S9. The final team pass plus individual implementation/review evidence is required for the bonus.

## Lint before opening a pull request

Install the same pinned linter as CI, then check the whole repository:

```sh
python -m pip install ruff==0.16.10
ruff check .
```

Every pull request runs separate `lint` and `tests` checks; both must pass before merging. Ruff checks Python errors and basic style, including student-added tests. Keep the supplied workflow and lint configuration unchanged.
