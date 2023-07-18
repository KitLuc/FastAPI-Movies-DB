from typing import Optional
from pydantic import BaseModel, Field


class User(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., min_length=1, max_length=100)
    email: str = Field(..., min_length=1, max_length=50, regex="^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}")
    password: str = Field(..., min_length=1, max_length=10)