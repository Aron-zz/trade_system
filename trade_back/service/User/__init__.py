from fastapi import APIRouter

from .auth import auth_router
from .check import check_router
from .get_info import get_info_router
from .register import register_router
from .update_info import update_info_router

user_router = APIRouter()
user_router.include_router(auth_router)
user_router.include_router(register_router)
user_router.include_router(check_router)
user_router.include_router(get_info_router)
user_router.include_router(register_router)
user_router.include_router(update_info_router)
