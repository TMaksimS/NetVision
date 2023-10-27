import uuid

from pydantic import BaseModel


class PostCreate(BaseModel):
    text: str


class ShowPost(BaseModel):
    uuid: uuid.UUID
    text: str
