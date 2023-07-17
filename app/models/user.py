from sqlalchemy import Column, Integer, String
from config.database import BASE


class User(BASE):
    __tablename__ = 'TBL_Users'
    id:Integer = Column(Integer, primary_key = True)
    name:String = Column(String, nullable = False)
    user:String = Column(String, nullable = False)
    password:String = Column(String, nullable = False)
    