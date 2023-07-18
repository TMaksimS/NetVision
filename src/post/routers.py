import uuid

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.encoders import jsonable_encoder

from src.database import get_db
from src.post.crud import PostBL

app = APIRouter()


@app.post("/new")
async def create_new_post(text: str, session: AsyncSession = Depends(get_db)):
    result = await PostBL.create_post(text=text, session=session)
    return jsonable_encoder(result)


@app.get("/all")
async def get_all_post(session: AsyncSession = Depends(get_db)):
    result = await PostBL.get_all_posts(session=session)
    return jsonable_encoder(result)


@app.get("/{uuid}")
async def get_current_post(uuid: uuid.UUID,
                           session: AsyncSession = Depends(get_db)):
    result = await PostBL.get_current_post(post_id=uuid, session=session)
    return jsonable_encoder(result)


@app.get("/all/{count}")
async def get_count_post(count: int, session: AsyncSession = Depends(get_db)):
    result = await PostBL.get_count_post(count=count, session=session)
    return jsonable_encoder(result)


@app.delete("/{uuid}")
async def delete_current_post(uuid: uuid.UUID,
                              session: AsyncSession = Depends(get_db)):
    result = await PostBL.delete_post(post_id=uuid, session=session)
    return JSONResponse(content=result, status_code=200)

