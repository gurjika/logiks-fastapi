from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import Optional

class Book(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    author: str
    year: str
    genre: Optional[str] = None