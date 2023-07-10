from fastapi import APIRouter

from app.api.api_v1.board import board_api

api_router = APIRouter()
api_router.include_router(board_api.router, tags=["Board API"])
