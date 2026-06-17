from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers.task import router as task_router
from app.api.routers.categories import router as category_router
from app.core.config import get_settings
from app.models.base import Base
from app.db.session import engine


# @asynccontextmanager
# async def lifespan(_: FastAPI):
#     from app.models.task import TaskORM
#     from app.models.categories import CategoryORM
#     yield


settings = get_settings()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(task_router)
app.include_router(category_router)

