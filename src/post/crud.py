import uuid

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, Sequence, Result

from src.post.shemas import ShowPost
from src.post.models import Post


class PostDB:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_post(self, text: str) -> Post:
        new_post = Post(text=text)
        self.session.add(new_post)
        await self.session.flush()
        return new_post

    async def get_current_post(self, post_id: uuid.UUID) -> Post:
        stmt = select(Post).where(Post.id == post_id)
        return await self.session.scalar(stmt)

    async def get_all_posts(self) -> Sequence:
        stmt = select(Post)
        result = await self.session.scalars(stmt)
        return result.all()

    async def get_count_post(self, count: int) -> Sequence:
        stmt = select(Post).limit(count)
        result = await self.session.scalars(stmt)
        return result.all()

    async def delete_post(self, post_id: uuid.UUID) -> Result:
        stmt = delete(Post).where(Post.id == post_id).returning(Post.id)
        return await self.session.execute(stmt)


class PostBL:
    @staticmethod
    async def create_post(text: str, session: AsyncSession) -> ShowPost:
        async with session.begin():
            connect = PostDB(session=session)
            post = await connect.create_post(text=text)
            return ShowPost(
                uuid=post.id,
                text=post.text
            )

    @staticmethod
    async def get_all_posts(session: AsyncSession) -> list[ShowPost]:
        async with session.begin():
            connect = PostDB(session=session)
            posts = await connect.get_all_posts()
            if posts:
                return [ShowPost(uuid=post.id, text=post.text)
                        for post in posts]
            else:
                raise HTTPException(status_code=204,
                                    detail={"message": "No Content"})

    @staticmethod
    async def get_current_post(post_id: uuid.UUID,
                               session: AsyncSession) -> ShowPost:
        async with session.begin():
            connect = PostDB(session=session)
            post = await connect.get_current_post(post_id=post_id)
            if post:
                return ShowPost(uuid=post.id,
                                text=post.text)
            else:
                raise HTTPException(status_code=404,
                                    detail={"message": "Incorrect request"})

    @staticmethod
    async def get_count_post(count: int,
                             session: AsyncSession) -> list[ShowPost]:
        async with session.begin():
            connect = PostDB(session=session)
            posts = await connect.get_count_post(count=count)
            if posts:
                return [ShowPost(uuid=post.id, text=post.text)
                        for post in posts]
            else:
                raise HTTPException(status_code=204,
                                    detail={"message": "No Content"})

    @staticmethod
    async def delete_post(post_id: uuid.UUID,
                          session: AsyncSession) -> dict:
        async with session.begin():
            connect = PostDB(session=session)
            data = await connect.get_current_post(post_id=post_id)
            if data:
                await connect.delete_post(post_id=post_id)
                return {"uuid": f"{post_id}",
                        "message": "Post has been deleted"}
            else:
                raise HTTPException(status_code=404,
                                    detail={"message": "Incorrect request"})
