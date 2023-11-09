from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

from app.data_classes.user_data_classes.user_data import UserData
from app.controllers.user_controller import userController


app = FastAPI()


@app.post("/login")
async def login(user_data: UserData):
    result = userController.login(user_data)
    return result
