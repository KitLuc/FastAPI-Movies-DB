import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from config.database import SESSION, ENGINE, BASE
from models.movie import Movie as MovieModel
from middlewares.error_handler import ErrorHandler


BASE.metadata.create_all(bind=ENGINE)
app = FastAPI()
app.title = ""
app.version = ""
app.add_middleware(ErrorHandler)


class Movie(BaseModel):
    id: int
    title: str
    year: int
    override: str
    director: str
    national: str
    gender: str
    budget: float




@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/movies/", status_code=200, response_model=list[Movie])
def get_movies() -> list[Movie]:
    DB = SESSION()
    movies = DB.query(MovieModel).all()
    return movies


@app.get("/movies/{director}", status_code=200)
def get_movie_by_director(director: str):
    DB = SESSION()
    movies = DB.query(MovieModel).filter(MovieModel.director == director).all()[0]
    return movies


@app.post("/movies/", status_code=201)
def create_movie(movie: Movie):
    new_movie = MovieModel(**movie.dict())
    DB = SESSION()
    DB.add(new_movie)
    DB.commit()
    return JSONResponse(status_code=201, content={"message": "Movie created"})


@app.put("/movies/{id}", status_code=200)
def update_movie(id: int, movie: Movie):
    DB = SESSION()
    query = DB.query(MovieModel).filter(MovieModel.id == id).first()
    
    if not query:
        return JSONResponse(status_code=404, content={"message": "Movie not found"})
    
    for key, value in movie.dict().items():
        setattr(query, key, value)
    DB.commit()
    return JSONResponse(status_code=200, content={"message": "Movie updated"})


@app.delete("/movies/{movie_id}", status_code=200)
def delete_movie(id: int) -> JSONResponse:
    DB = SESSION()
    movie = DB.query(MovieModel).filter(MovieModel.id == id).first()
    DB.delete(movie)
    DB.commit()
    return JSONResponse(status_code=200, content={"message": "Movie deleted"})


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=1234, reload=True, workers=2)