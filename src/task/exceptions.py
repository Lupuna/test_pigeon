class TaskError(Exception):
    def __init__(self, object_name: str | int | None = None):
        self.object_name = object_name


class TaskNotFoundError(TaskError): ...
