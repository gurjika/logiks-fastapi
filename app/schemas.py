from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import Optional

class BookBase(BaseModel):
    title: str
    author: str
    year: int
    genre: Optional[str] = None



class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        from_attributes = True