from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    id: Optional[int] = None 
    title: str = Field(..., min_length=1, max_length=100)
    year: int = Field(..., gt=1900, lt=2025)
    override: str = Field(..., min_length=1, max_length=100)
    director: str = Field(..., min_length=1, max_length=100)
    national: str = Field(..., min_length=1, max_length=3)
    gender: str = Field(..., min_length=1, max_length=80)
    budget: float = Field(..., gt=0)
    
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "title": "The Godfather",
                "year": 1972,
                "override": "R",
                "director": "Francis Ford Coppola",
                "national": "USA",
                "gender": "Crime, Drama",
                "budget": 6000000.0  
            }
        }