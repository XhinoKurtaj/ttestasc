from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.api import api_router
from db.models import metadata
from core.config import settings

app = FastAPI()

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


# metadata.create_all(bind=engine)
app.include_router(api_router, prefix=settings.API_V1_STR)


# from fastapi import FastAPI
# from project.routers.users import router as users_router
# from project.routers.posts import router as posts_router

# app = FastAPI()

# app.include_router(posts_router(), prefix="/posts", tags=['posts'])
# app.include_router(posts_router(), prefix="/users", tags=['users'])