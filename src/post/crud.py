import uuid

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from src.post.shemas import PostCreate, ShowPost
from src.post.models import Post


class PostDB:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_post(self, text: str) -> Post:
        new_post = Post(text=text)
        self.session.add(new_post)
        await self.session.flush()
        return new_post

    async def get_current_post(self, post_id: uuid.UUID) -> ShowPost:
        pass

    async def get_all_posts(self) -> list:
        pass

    async def get_count_post(self, count: int) -> list:
        pass

    async def delete_post(self, post_id: uuid.UUID) -> ShowPost:
        pass


class PostBL:
    @staticmethod
    async def create_post(text: str, session: AsyncSession) -> ShowPost:
            connect = PostDB(session=session)
            post = await connect.create_post(text=text)
            return ShowPost(
                post_id=post.id,
                text=post.text
            )
