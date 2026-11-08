from fastapi import APIRouter

from endpoints import health, login, users

api_router = APIRouter()
api_router.include_router(health.router)
api_router.include_router(users.router)
api_router.include_router(login.router)