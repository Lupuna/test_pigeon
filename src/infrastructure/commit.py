import functools
from typing import Any, Callable, Coroutine

def commitable(
    commitable_method: Callable[..., Coroutine],
) -> Callable[..., Coroutine]:
    @functools.wraps(commitable_method)
    async def commit(self, *args, **kwargs) -> Any:
        do_commit = kwargs.pop("commit", True)
        result = await commitable_method(self, *args, **kwargs)
        if do_commit:
            await self.session.commit()
        return result

    return commit
