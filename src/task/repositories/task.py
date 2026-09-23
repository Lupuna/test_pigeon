from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.commit import commitable
from task.models import Task
from task.schemas import DBTaskSchema, TaskSchema


class TaskRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_id(self, task_id: int) -> DBTaskSchema | None:
        task = await self.session.get(Task, task_id)
        return DBTaskSchema.model_validate(task) if task is not None else None

    async def get_all(self, is_completed: bool | None = None) -> list[DBTaskSchema]:
        stmt = select(Task)
        if is_completed is not None:
            stmt = stmt.where(Task.is_completed == is_completed)
        result = await self.session.execute(stmt)
        return [DBTaskSchema.model_validate(task) for task in result.scalars().all()]

    @commitable
    async def create(self, data: TaskSchema) -> DBTaskSchema:
        task = Task(**data.model_dump())
        self.session.add(task)
        await self.session.flush()
        return DBTaskSchema.model_validate(task)

    @commitable
    async def update(self, task_id: int, **values) -> DBTaskSchema | None:
        result = await self.session.execute(
            update(Task).where(Task.id == task_id).values(**values).returning(Task)
        )
        task = result.scalar_one_or_none()
        return DBTaskSchema.model_validate(task) if task is not None else None

    @commitable
    async def delete(self, task_id: int) -> None:
        await self.session.execute(delete(Task).where(Task.id == task_id))
