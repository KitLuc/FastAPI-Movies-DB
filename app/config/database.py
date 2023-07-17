import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQL_URI = '../database/DB_MoviesFastAPI.sqlite'
DIR = os.path.dirname(os.path.realpath(__file__))
DATABASE_URI = 'sqlite:///' + os.path.join(DIR, SQL_URI)
ENGINE = create_engine(DATABASE_URI, echo = True)
SESSION = sessionmaker(bind = ENGINE)
BASE = declarative_base()
