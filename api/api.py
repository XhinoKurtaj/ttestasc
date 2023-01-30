from fastapi import APIRouter

from api.endpoints import timer_api

api_router = APIRouter()
api_router.include_router(timer_api.router, prefix="/time", tags=["time"])
