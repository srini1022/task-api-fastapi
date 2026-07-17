from app.database import get_connection


def get_all_tasks():
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, title, done FROM tasks"
    )

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    tasks = []

    for row in rows:
        tasks.append({
            "id": row[0],
            "title": row[1],
            "done": row[2]
        })

    return tasks

def get_task_by_id(task_id: int):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, title, done FROM tasks WHERE id = %s",
        (task_id,)
    )

    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if row is None:
        return None

    return {
        "id": row[0],
        "title": row[1],
        "done": row[2]
    }

def create_task(title: str):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO tasks (title, done)
        VALUES (%s, %s)
        RETURNING id, title, done
        """,
        (title, False)
    )

    row = cursor.fetchone()

    conn.commit()

    cursor.close()
    conn.close()

    return {
        "id": row[0],
        "title": row[1],
        "done": row[2]
    }

def update_task(task_id: int, title: str, done: bool):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE tasks
        SET title = %s, done = %s
        WHERE id = %s
        RETURNING id, title, done
        """,
        (title, done, task_id)
    )

    row = cursor.fetchone()

    conn.commit()

    cursor.close()
    conn.close()

    if row is None:
        return None

    return {
        "id": row[0],
        "title": row[1],
        "done": row[2]
    }

def delete_task(task_id: int):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tasks WHERE id = %s RETURNING id",
        (task_id,)
    )

    row = cursor.fetchone()

    conn.commit()

    cursor.close()
    conn.close()

    return row is not None