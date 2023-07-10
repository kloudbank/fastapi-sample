from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class BoardBase(BaseModel):
    userid: str = 'ia02736'
    title: str = 'Title'
    content: Optional[str] = 'Contents,,'

class BoardCreate(BoardBase):
    pass

class BoardUpdate(BoardBase):
    pass

class Board(BoardBase):
    id: int
    createdat: datetime
    updatedat: datetime
    class Config:
        orm_mode = True
