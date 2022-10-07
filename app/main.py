from fastapi import FastAPI

from app.api import items

app = FastAPI()

app.include_router(items.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
