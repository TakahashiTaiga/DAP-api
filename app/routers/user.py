from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

from app.data_classes.user_data_classes.user_data import UserData
from app.controllers.user_controller import userController as uc


app = FastAPI()


@app.post("/signup/")
async def signup(userdata: UserData):
    result = uc.signup(userdata)
    return result
