from fastapi import APIRouter, HTTPException
from app.schemas.task import TaskCreate, TaskUpdate
from app.services.task_service import (
    get_all_tasks,
    get_task_by_id,
    create_task,
    update_task,
    delete_task
)
router = APIRouter()


@router.get("/tasks")
def get_tasks():
    return get_all_tasks()

@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = get_task_by_id(task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task

@router.post("/tasks", status_code=201)
def add_task(task: TaskCreate):
    return create_task(task.title)

@router.put("/tasks/{task_id}")
def edit_task(task_id: int, task: TaskUpdate):

    updated_task = update_task(
        task_id,
        task.title,
        task.done
    )

    if updated_task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return updated_task

from fastapi import Response

@router.delete("/tasks/{task_id}", status_code=204)
def remove_task(task_id: int):

    deleted = delete_task(task_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return Response(status_code=204)

