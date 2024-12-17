from fastapi import APIRouter

from .get_info import get_info_router
from .update_info import update_info_router

record_router = APIRouter()
record_router.include_router(get_info_router)
record_router.include_router(update_info_router)
