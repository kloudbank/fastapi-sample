from fastapi import HTTPException
from sqlalchemy.orm import Session

from . import board_model, board_schema

def get_board_all(db: Session):
    return db.query(board_model.Board).all()

def get_board_by_id(id: int, db: Session):
    db_board = db.query(board_model.Board).filter(board_model.Board.id == id).first()
    if db_board is None:
        raise HTTPException(status_code=404, detail="Board not found")
    return db_board

def create_board(db: Session, board: board_schema.BoardCreate):
    db_board = board_model.Board(**board.dict())
    db.add(db_board)
    db.commit()
    db.refresh(db_board)
    return db_board

def update_board_by_id(id: int, db: Session, board: board_schema.BoardUpdate):
    db_board = db.query(board_model.Board).filter(board_model.Board.id == id)
    if db_board.first() is None:
        raise HTTPException(status_code=404, detail="Board not found")
    db_board.update(board.dict())
    db.commit()
    return db_board.first()

def delete_board_by_id(id: int, db: Session):
    db_board = db.query(board_model.Board).filter(board_model.Board.id == id)
    if db_board.first() is None:
        raise HTTPException(status_code=404, detail="Board not found")
    db_board.delete()
    db.commit()
    return True
