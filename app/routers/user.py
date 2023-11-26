from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

from app.data_classes.user_data_classes.user_data import UserData
from app.controllers.user_controller import userController


app = FastAPI()

"""
    ユーザー登録
    paramater:
        email str
        password str
    return:
        user_id int
"""


@app.post("/sing-up")
async def sing_up(user_data: UserData):
    result = userController.sign_up(user_data)

"""
    ログイン
    paramater:
        email str
        password str
    return:
        user_id int
"""


@app.post("/login")
async def login(user_data: UserData):
    login_dto = userController.login(user_data)
    return login_dto
