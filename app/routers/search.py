from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

from app.data_classes.search_data_classes.search_data import SearchConditions
from app.controllers.search_controller import searchController


app = FastAPI()


@app.post("/search")
async def search(search_conditions: SearchConditions):
    result = searchController.search(search_conditions)
    return result
