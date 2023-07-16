import uvicorn
from fastapi import FastAPI

from src.post.routers import app as post_router


app = FastAPI()


@app.get("/")
async def start():
    return {"message": "Hello World!"}

app.include_router(post_router, prefix="/post", tags=["post"])


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
