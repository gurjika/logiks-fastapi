import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from .config import settings


DB_PASSWORD = settings.db_password
DB_NAME = settings.db_name
DB_USER = settings.db_user


SQLALCHEMY_DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_NAME}/postgres'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()



def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
