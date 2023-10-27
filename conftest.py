import asyncio
import uuid
from typing import Generator, AsyncGenerator, Any

import asyncpg
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from src.database import get_db
from settings import REAL_DATABASE_URL
from main import app


async def get_db_test() -> AsyncGenerator[AsyncSession, None]:
    try:
        engine_test = create_async_engine(
            REAL_DATABASE_URL, echo=True)
        async_session_maker = sessionmaker(
            engine_test,
            class_=AsyncSession,
            expire_on_commit=False
        )
        yield async_session_maker()
    finally:
        pass


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def client() -> Generator[TestClient, Any, None]:
    app.dependency_overrides[get_db] = get_db_test
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="session")
async def async_session_test():
    engine = create_async_engine(
        REAL_DATABASE_URL,
        future=True,
        echo=True
    )
    async_session = sessionmaker(
        engine,
        expire_on_commit=False,
        class_=AsyncSession
    )
    yield async_session


@pytest.fixture(scope="session")
async def asyncpg_pool():
    pool = await asyncpg.create_pool(
        "".join(REAL_DATABASE_URL.split("+asyncpg"))
    )
    yield pool
    await pool.close()


@pytest.fixture
async def get_post_from_db(asyncpg_pool):
    async def get_post_by_text(text: str):
        async with asyncpg_pool.acquire() as connection:
            return await connection.fetch(
                """SELECT * FROM posts WHERE text = $1;""", text
            )

    return get_post_by_text


@pytest.fixture
async def create_post_in_db(asyncpg_pool):
    async def create_post(id: uuid.UUID, text: str):
        async with asyncpg_pool.acquire() as connection:
            return await connection.execute(
                """INSERT INTO posts VALUES ($1, $2)""",
                id,
                text,
            )

    return create_post
