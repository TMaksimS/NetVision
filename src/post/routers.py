from fastapi import APIRouter, Depends, HTTPException



app = APIRouter()


@app.post("/new")
async def create_new_post():
    pass


@app.get("/all")
async def get_all_post():
    pass


@app.get("/<uuid>")
async def get_current_post():
    pass


@app.get("/<count>")
async def get_count_post():
    pass


@app.delete("/<uuid>")
async def delete_current_post():
    pass
