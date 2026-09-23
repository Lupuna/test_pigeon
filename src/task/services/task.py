from task.exceptions import TaskNotFoundError
from task.repositories import TaskRepository
from task.schemas import DBTaskSchema, TaskSchema, TaskUpdateSchema


class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    async def get(self, task_id: int) -> DBTaskSchema:
        task = await self.repository.get_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)
        return task

    async def get_all(self, is_completed: bool | None = None) -> list[DBTaskSchema]:
        return await self.repository.get_all(is_completed=is_completed)

    async def create(self, data: TaskSchema) -> DBTaskSchema:
        return await self.repository.create(data)

    async def update(self, task_id: int, data: TaskUpdateSchema) -> DBTaskSchema:
        task = await self.repository.update(task_id, **data.model_dump())
        if task is None:
            raise TaskNotFoundError(task_id)
        return task

    async def complete(self, task_id: int) -> DBTaskSchema:
        task = await self.repository.update(task_id, is_completed=True)
        if task is None:
            raise TaskNotFoundError(task_id)
        return task

    async def delete(self, task_id: int) -> None:
        await self.repository.delete(task_id)
