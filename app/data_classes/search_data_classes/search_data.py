from pydantic import BaseModel


class SearchConditions(BaseModel):
    free_bar: str
    owner: str
    attributes: dict
