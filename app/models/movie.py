from sqlalchemy import Column, Integer, String, Float
from config.database import BASE


class Movie(BASE):
    __tablename__ = 'TBL_Movies'
    id: int = Column(Integer, primary_key = True, autoincrement=1)
    title: str = Column(String, nullable = False)
    year: int = Column(Integer, nullable = False)
    override: str = Column(String, nullable = False)
    national: str = Column(String, nullable = False)
    gender: str = Column(String, nullable=False)
    budget: float = Column(Float, nullable = False)
    director: str = Column(String, nullable = False)