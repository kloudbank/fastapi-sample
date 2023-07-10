from fastapi import Depends
from fastapi.routing import APIRouter
from . import board_crud, board_schema
from sqlalchemy.orm import Session
from app.core.database import SessionLocal, get_db


router = APIRouter(prefix='/board')

@router.get("/all", response_model=list[board_schema.Board])
def read_users(db: Session = Depends(get_db)):
    return board_crud.get_board_all(db)

@router.get("/{id}", response_model=board_schema.Board)
def get_board_by_id(id: int, db: Session = Depends(get_db)):
    return board_crud.get_board_by_id(id, db)

@router.post("/", response_model=board_schema.Board)
def create_board(board: board_schema.BoardCreate, db: Session = Depends(get_db)):
    return board_crud.create_board(db, board)

@router.put("/{id}", response_model=board_schema.Board)
def edit_board_by_id(id: int, board: board_schema.BoardUpdate, db: Session = Depends(get_db)):
    return board_crud.update_board_by_id(id, db, board)

@router.delete("/{id}")
def delete_board_by_id(id: int, db: Session = Depends(get_db)):
    return board_crud.delete_board_by_id(id, db)
