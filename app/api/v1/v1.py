from fastapi import APIRouter
from app.api.endpoints.friends import friends_router
from app.api.endpoints.schedule import schedule_router
from app.api.endpoints.user_profile import profile_router

v1_router = APIRouter()

v1_router.include_router(friends_router)
v1_router.include_router(schedule_router)
v1_router.include_router(profile_router)
