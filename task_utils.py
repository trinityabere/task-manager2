from validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

tasks = []

def add_task(title, description, due_date, priority):
    if (
        validate_task_title(title)
        and validate_task_description(description)
        and validate_due_date(due_date)
    ):
        task = {
            "title": title,
            "description": description,
            "due_date": due_date,
            "priority": priority,
            "completed": False
        }
        tasks.append(task)
        return "Task added successfully!"
    else:
        return "Invalid task details."


def mark_task_as_complete(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        return "Task marked as complete!"
    return "Invalid task index."


def view_pending_tasks():
    output = []
    for i, task in enumerate(tasks):
        if not task["completed"]:
            output.append(
                f"{i}. {task['title']} - {task['description']} (Due: {task['due_date']})"
            )
    return output if output else ["No pending tasks."]


def calculate_progress():
    if len(tasks) == 0:
        return 0
    completed = sum(1 for t in tasks if t["completed"])
    return (completed / len(tasks)) * 100