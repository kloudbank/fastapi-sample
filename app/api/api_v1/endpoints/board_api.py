from fastapi.routing import APIRouter
from typing import Optional
from app.core.config import settings

router = APIRouter(prefix='/board')

@router.get("/all")
def get_board_all():
    return {"app_env": settings.APP_ENV, "project_name": settings.PROJECT_NAME}


@router.get("/{id}")
def get_board_by_id(id: int):
    return {"id": id}

@router.post("/")
def create_board():
    return "created"

@router.put("/{id}")
def edit_board_by_id(id: int):
    return {"id": id}

@router.delete("/{id}")
def delete_board_by_id(id: int):
    return {"id": id}
