from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

from app.controllers.directory_controller import directoryController


app = FastAPI()


@app.get("/top")
async def top():
    result = directoryController.top()
    return result


@app.get("/file/{file_path}")
async def file(file_path: str):
    result = directoryController.file(file_path)
    return result
