from fastapi import FastAPI

from task.exception_handlers import register_task_exception_handlers
from task.routers.task import router as task_router

app = FastAPI()

register_task_exception_handlers(app)
app.include_router(task_router)
