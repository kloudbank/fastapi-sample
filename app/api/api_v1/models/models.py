from sqlalchemy import Column, Integer, String, DATETIME, func
from sqlalchemy.orm import relationship

from app.core.database import Base


class Board(Base):
    __tablename__ = "board"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    userid = Column(String)
    title = Column(String)
    content = Column(String)
    createdat = Column(DATETIME, server_default=func.now())
    updatedat = Column(DATETIME, onupdate=func.now())
