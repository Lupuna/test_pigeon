from fastapi import APIRouter, Depends, status

from task.deps import get_task_service
from task.schemas import DBTaskSchema, TaskSchema, TaskUpdateSchema
from task.services import TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("", response_model=list[DBTaskSchema])
async def get_tasks(
    is_completed: bool | None = None,
    service: TaskService = Depends(get_task_service),
) -> list[DBTaskSchema]:
    return await service.get_all(is_completed=is_completed)


@router.get("/{task_id}", response_model=DBTaskSchema)
async def get_task(
    task_id: int,
    service: TaskService = Depends(get_task_service),
) -> DBTaskSchema:
    return await service.get(task_id)


@router.post("", response_model=DBTaskSchema, status_code=status.HTTP_201_CREATED)
async def create_task(
    payload: TaskSchema,
    service: TaskService = Depends(get_task_service),
) -> DBTaskSchema:
    return await service.create(payload)


@router.put("/{task_id}", response_model=DBTaskSchema)
async def update_task(
    task_id: int,
    payload: TaskUpdateSchema,
    service: TaskService = Depends(get_task_service),
) -> DBTaskSchema:
    return await service.update(task_id, payload)


@router.patch("/{task_id}/complete", response_model=DBTaskSchema)
async def complete_task(
    task_id: int,
    service: TaskService = Depends(get_task_service),
) -> DBTaskSchema:
    return await service.complete(task_id)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: int,
    service: TaskService = Depends(get_task_service),
) -> None:
    await service.delete(task_id)
