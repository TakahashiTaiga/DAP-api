from fastapi import FastAPI

from api.routers import data, directory, search, user

app = FastAPI()
app.include_router(data.router)
app.include_router(directory.router)
app.include_router(search.router)
app.include_router(user.router)
