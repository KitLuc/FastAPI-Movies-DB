from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from config.database import SESSION
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie


movie = APIRouter()


@movie.get("/movies/", status_code=200, response_model=list[Movie])
def get_movies() -> list[Movie]:
    DB = SESSION()
    movies = MovieService(DB).get_movies()
    return movies


@movie.get("/movies/{director}", status_code=200)
def get_movie_by_director(director: str):
    DB = SESSION()
    movies = MovieService(DB).get_movie(director)[0]
    return movies


@movie.post("/movies/", status_code=201, dependencies=[Depends(JWTBearer())])
def create_movie(movie: Movie):
    DB = SESSION()
    MovieService(DB).create_movie(movie)
    return JSONResponse(status_code=201, content={"message": "Movie created"})


@movie.put("/movies/{id}", status_code=200, dependencies=[Depends(JWTBearer())])
def update_movie(id: int, movie: Movie):
    DB = SESSION()
    MovieService(DB).update_movie(id, movie)
    return JSONResponse(status_code=200, content={"message": "Movie updated"})


@movie.delete("/movies/{movie_id}", status_code=200, dependencies=[Depends(JWTBearer())])
def delete_movie(id: int) -> JSONResponse:
    DB = SESSION()
    MovieService(DB).delete_movie(id)
    return JSONResponse(status_code=200, content={"message": "Movie deleted"})
