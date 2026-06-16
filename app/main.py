from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routers.task import router
from app.api.routers.categories import routers
from app.core.config import get_settings
from app.models.base import Base
from app.db.session import engine


@asynccontextmanager
async def lifespan(_: FastAPI):
    from app.models.task import TaskORM
    from app.models.categories import CategoryORM
    Base.metadata.create_all(bind=engine)
    yield


settings = get_settings()
app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(router)
app.include_router(routers)

