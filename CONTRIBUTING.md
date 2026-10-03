# Pull Request Relay: student handout

Your team owns one small Python application. Across three rounds you will implement changes, review a teammate's work, and merge approved PRs. Follow your assigned role each round; everyone will both author and review during the lab.

## Before the first round

1. Confirm access to your team's GitHub repository. Clone it and open the folder.
2. Check `python3 --version` (3.11 or later) and `git --version`. On Windows, use `python` or `py` instead of `python3` if needed.
3. Run `python3 app.py`, then `python3 check.py`. The starter checks should pass.
4. Find your task ID, reviewer, and specification in the assignment sheet and `TASKS.md`.

The project contains a working demo, some missing features, and three deliberately incomplete functions for round two. All acceptance tests are visible. The full final suite is expected to fail on the starter.

## When you are the author

Start each task from current `main`. Use your own assigned task ID in every example below (the example uses `E1`).

```sh
git switch main
git pull --ff-only
git switch -c task/E1-your-github-name
python3 check.py --task E1
# Implement the function in app.py. Add a meaningful test in tests/test_student_E1.py.
# Then run the focused checks again; they should now pass.
python3 check.py --task E1
# Enable your task's acceptance tests permanently in CI.
python3 check.py --complete E1
git status
git diff
git add app.py tests/test_student_E1.py completed/E1.txt
git commit -m "E1: summarize expenses by category"
git push -u origin task/E1-your-github-name
```

Create a GitHub PR targeting `main`, put the task ID in the title, fill in the PR template, and request the assigned reviewer. Include the problem, implementation, test command and result. Include a normal case and an edge case in your explanation. Round-two authors must show a regression test failing before the fix and passing afterwards.

Do the assigned task only. Preserve earlier behavior. Do not change supplied acceptance tests, `check.py`, `tasks.json`, or the CI workflow. You may add tests in `tests/test_student_<TASK>.py`. Reviewers should verify the diff respects this rule.

You can push follow-up commits to the same PR after feedback. Each update must pass checks and receive a current approval. Keep your task marker; never remove another task's marker to turn CI green.

## When you are the reviewer and merger

Read the specification before the implementation. Check the whole diff, run the tests locally, and verify at least one edge case yourself. You may review two small PRs in a five-person team.

To check a teammate's branch without replacing your own work:

```sh
# First commit your own work, or use a separate clone if your working tree is dirty.
git fetch origin
git switch --track origin/task/E1-author-github-name
python3 check.py
python3 check.py --task E1
```

If that local branch already exists, use `git switch <branch>` and `git pull --ff-only`. After your review, switch back to your own branch or `main`.

A substantive review names something you actually checked. For example: “The empty list returns `{}`, and two expenses in the same category are added correctly. I ran `python3 check.py --task E1`. The diff preserves the input list. Approved.” If the change is wrong, use **Request changes** and explain a reproducible example plus the expected behavior. Do not invent a defect merely to write a comment.

Merge only when the specification is satisfied, CI is green, the branch is up to date, discussion is resolved, and your approval covers the latest changes. The assigned reviewer performs the merge; the author must not approve their own PR. Use the GitHub merge button, then all teammates pull current `main` before the next task. An approval with no evidence such as “LGTM” does not count as a substantive review.

## Round three: keep everyone's changes

All three authors must branch from the same current `main` **before anyone merges**. Each author also replaces the single line `Round 3 features: none.` in `RELEASE_NOTES.md`, adding their task ID. This creates a small, intentional shared-file conflict. When a teammate's change lands first:

```sh
git fetch origin
git merge origin/main
# Edit RELEASE_NOTES.md, preserving every completed round-three ID on one line.
# Example: Round 3 features: E7, E8, E9.
# Remove conflict markers and preserve both authors' implementations.
git add RELEASE_NOTES.md app.py
git commit
python3 check.py
git push
```

If Git completed the merge automatically, there is no separate conflict-resolution commit to make. Do not use force-push or overwrite the other branch. Ask for review again after resolving the conflict. Include `RELEASE_NOTES.md` in your round-three task commit.

## Finish together

After all nine PRs have merged, everyone pulls `main`. Run:

```sh
python3 check.py --all
```

Use the final repair window to fix any failures through reviewed PRs. A repair can also provide an implementation or review opportunity to someone whose original task was blocked. Give the instructor a merged implementation PR link and a link to your substantive review.

**Bonus:** one point only if your final team `main` passes the entire acceptance suite and your individual implementation and review are verified. Unfinished tasks still fail the final check even if they have no completion marker. The instructor grades the final committed version at the deadline; a green feature branch does not count.

