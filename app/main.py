from fastapi import FastAPI

from app.routers import directory, search, user

app = FastAPI()
app.include_router(directory.router)
app.include_router(search.router)
app.include_router(user.router)
