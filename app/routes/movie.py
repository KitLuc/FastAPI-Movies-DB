from fastapi import APIRouter
from fastapi.responses import JSONResponse
from config.database import SESSION
from models.movie import Movie as MovieModel
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie


app = APIRouter()


@app.get("/movies/", status_code=200, response_model=list[Movie])
async def get_movies() -> list[Movie]:
    DB = SESSION()
    movies = await MovieService(DB).get_movies()
    return movies


@app.get("/movies/{director}", status_code=200)
async def get_movie_by_director(director: str):
    DB = SESSION()
    movies = await MovieService(DB).get_movies(director)[0]
    return movies


@app.post("/movies/", status_code=201)
async def create_movie(movie: Movie):
    DB = SESSION()
    await MovieService(DB).create_movie(movie)
    return JSONResponse(status_code=201, content={"message": "Movie created"})


@app.put("/movies/{id}", status_code=200)
async def update_movie(id: int, movie: Movie):
    DB = SESSION()
    result = await MovieService(DB).update_movie(id, movie)
    
    if not result:
        return JSONResponse(status_code=404, content={"message": "Movie not found"})
    return JSONResponse(status_code=200, content={"message": "Movie updated"})


@app.delete("/movies/{movie_id}", status_code=200)
async def delete_movie(id: int) -> JSONResponse:
    DB = SESSION()
    result = await MovieService(DB).delete_movie(id)
    
    if not result:
        return JSONResponse(status_code=404, content={"message": "Movie not found"})
    return JSONResponse(status_code=200, content={"message": "Movie deleted"})
