from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class TaskSchema(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=255)


class TaskUpdateSchema(TaskSchema):
    is_completed: bool = Field(default=False)


class DBTaskSchema(TaskSchema):
    model_config = ConfigDict(from_attributes=True)

    id: int
    is_completed: bool
    created_at: datetime
