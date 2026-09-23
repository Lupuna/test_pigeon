from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.deps import get_db
from task.repositories import TaskRepository
from task.services import TaskService


def get_task_repository(session: AsyncSession = Depends(get_db)) -> TaskRepository:
    return TaskRepository(session)


async def get_task_service(
    repo: TaskRepository = Depends(get_task_repository),
) -> TaskService:
    return TaskService(repo)
