from app.data.task_store import tasks


def get_all_tasks():
    return tasks


def get_task_by_id(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

def create_task(title: str):
    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "done": False
    }

    tasks.append(new_task)

    return new_task

def update_task(task_id: int, title: str, done: bool):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = title
            task["done"] = done
            return task

    return None

def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return True

    return False