from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class TaskSchema(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None, max_length=255)


class TaskUpdateSchema(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    description: str | None = Field(max_length=255)
    is_completed: bool


class DBTaskSchema(TaskSchema):
    model_config = ConfigDict(from_attributes=True)

    id: int
    is_completed: bool
    created_at: datetime
