from sqlalchemy import Column, Integer, String, TIMESTAMP, func

from app.core.database import Base


class Board(Base):
    __tablename__ = "board"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    userid = Column(String)
    title = Column(String)
    content = Column(String)
    createdat = Column(TIMESTAMP, server_default=func.now())
    updatedat = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
