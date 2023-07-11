from fastapi import APIRouter

from app.api.api_v1.board import board_api
from app.api.api_v1.account import account_api

api_router = APIRouter()
api_router.include_router(board_api.router, tags=["Board API"])
api_router.include_router(account_api.router, tags=["Account API"])
