from models.movie import Movie as MovieModel
from schemas.movie import Movie


class MovieService:
    def __init__(self, DB) -> None:
        self.DB = DB

    def get_movies(self):
        result = self.DB.query(MovieModel).all()
        return result

    def get_movies(self, director):
        result = self.DB.query(MovieModel).filter(MovieModel.director == director).all()
        return result

    def create_movie(self, movie: Movie):
        new_movie = MovieModel(**movie.dict())
        self.DB.add(new_movie)
        self.DB.commit()
        return

    def update_movie(self, id: int, movie: Movie):
        query = self.DB.query(MovieModel).filter(MovieModel.id == id).first()

        for key, value in movie.dict().items():
            setattr(query, key, value)

        self.DB.commit()
        return

    def delete_movie(self, id: int):
        query = self.DB.query(MovieModel).filter(MovieModel.id == id).delete()
        self.DB.commit()
        return
