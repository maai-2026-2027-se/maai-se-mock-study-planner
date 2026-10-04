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
    if not tasks:
        return 0.0
    done_count = sum(1 for task in tasks if task['done'])
    print(f"Done count: {done_count}, Total tasks: {len(tasks)}")
    print(f"Completion rate (before rounding): {(done_count / len(tasks)) * 100}")
    result = round((done_count / len(tasks)) * 100, 1)
    print(f"Completion rate (after rounding): {result}")
    return result


def find_tasks(tasks, query):
    """S3: Search task titles. See TASKS.md for the complete contract."""
    normalized_query = query.strip().casefold()
    if not normalized_query:
        return list(tasks)
    return [task for task in tasks if normalized_query in task['title'].casefold()]


def mark_done(tasks, title):
    """S4: Fix task completion without mutation. See TASKS.md for the complete contract."""
    if not any(task['title'] == title for task in tasks):
        raise KeyError(title)

    updated_tasks = []
    for task in tasks:
        updated_task = dict(task)
        if task['title'] == title:
            updated_task['done'] = True
        updated_tasks.append(updated_task)
    return updated_tasks


def estimate_sessions(minutes, block_minutes):
    """S5: Fix session estimates. See TASKS.md for the complete contract."""
    if minutes < 0 or block_minutes <= 0:
        raise ValueError("minutes must be nonnegative and block_minutes must be positive")
    return (minutes + block_minutes - 1) // block_minutes


def sort_tasks(tasks):
    """S6: Fix priority ordering. See TASKS.md for the complete contract."""
    return sorted(tasks, key=lambda task: (-task['minutes'], task['title'].casefold()))


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
