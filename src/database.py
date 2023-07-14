from typing import AsyncGenerator

from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncAttrs

DB_URL = f"postgresql+asyncpg://postgres:postgres@0.0.0.0:5432/postgres"

engine = create_async_engine(DB_URL, echo=True)
async_session_maker = sessionmaker(engine, expire_on_commit=False,
                                   class_=AsyncSession)


class Base(AsyncAttrs, DeclarativeBase):
    pass


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    try:
        async with async_session_maker() as session:
            yield session
    finally:
        await session.close()
