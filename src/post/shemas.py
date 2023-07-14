import uuid

from pydantic import BaseModel


class PostCreate(BaseModel):
    text: str


class ShowPost(PostCreate):
    post_id: uuid.UUID

