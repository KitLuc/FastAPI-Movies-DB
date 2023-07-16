import uvicorn
from fastapi import FastAPI

from config.database import SESSION, ENGINE, BASE
from models.movie import Movie as MovieModel

from pydantic import BaseModel, Field


class Movie(BaseModel):
    id: int = Field(
        ..., gt=0, description="Id de la pelicula"
    )
    title: str = Field(..., min_length=1, max_length=50)  # Validando longitud
    year: int = Field(..., gt=1900, lt=2100)  # Validando rango
    director: str = Field(..., min_length=1, max_length=50)
    override: str = Field(..., min_length=1, max_length=50)
    national: str = Field(..., min_length=1, max_length=50)
    gender: str = Field(..., min_length=1, max_length=50)
    budget: float = Field(..., gt=1000000, lt=1000000000)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Spiderman: Lejos de casa",
            }
        }



app = FastAPI()
BASE.metadata.create_all(bind=ENGINE)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/movies/", tags=["movies"], status_code=201)
def create_movie(movie: Movie):
    DB = SESSION()
    movie = MovieModel(**movie.dict())
    DB.add(movie)
    DB.commit()
    return "Movie created successfully"

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=1234, reload=True, workers=2)
    
    