from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from task.exceptions import TaskNotFoundError


async def task_not_found(_: Request, exc: TaskNotFoundError) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": f"{exc.object_name} not found"},
    )


def register_task_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(TaskNotFoundError, task_not_found)
