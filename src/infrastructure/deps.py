from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.database import async_session_factory


async def get_db() -> AsyncSession:
    async with async_session_factory() as session:
        yield session
