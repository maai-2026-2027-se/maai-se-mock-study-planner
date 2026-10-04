"""Study Planner: a small standard-library-only teaching project."""
import csv  # noqa: F401 -- available for the round-three CSV task
import io  # noqa: F401 -- available for the round-three CSV task
import json


def total_minutes(tasks):
    """Existing working behavior; preserve it while adding features."""
    return sum(task['minutes'] for task in tasks)


def pending_tasks(tasks):
    """S1: Find pending tasks. See TASKS.md for the complete contract."""
    return [task for task in tasks if not task['done']]


def completion_rate(tasks):
    """S2: Calculate completion percentage. See TASKS.md for the complete contract."""
    raise NotImplementedError("Implement S2: Calculate completion percentage")


def find_tasks(tasks, query):
    """S3: Search task titles. See TASKS.md for the complete contract."""
    raise NotImplementedError("Implement S3: Search task titles")


def mark_done(tasks, title):
    """S4: Fix task completion without mutation. See TASKS.md for the complete contract."""
    for task in tasks:
        if task['title'] == title:
            task['done'] = True
    return tasks


def estimate_sessions(minutes, block_minutes):
    """S5: Fix session estimates. See TASKS.md for the complete contract."""
    return minutes // block_minutes


def sort_tasks(tasks):
    """S6: Fix priority ordering. See TASKS.md for the complete contract."""
    return sorted(tasks, key=lambda task: task['minutes'])


def daily_plan(tasks, budget_minutes):
    """S7: Build a daily plan. See TASKS.md for the complete contract."""
    raise NotImplementedError("Implement S7: Build a daily plan")


def statistics(tasks):
    """S8: Build study statistics. See TASKS.md for the complete contract."""
    raise NotImplementedError("Implement S8: Build study statistics")


def to_csv(tasks):
    """S9: Export study tasks to CSV. See TASKS.md for the complete contract."""
    raise NotImplementedError("Implement S9: Export study tasks to CSV")


if __name__ == "__main__":
    example = [{'title': 'Git', 'minutes': 30, 'done': False}, {'title': 'Python', 'minutes': 45, 'done': True}, {'title': 'Tests', 'minutes': 20, 'done': False}]
    print(json.dumps(example, indent=2))
    print("total_minutes:", total_minutes(example))
