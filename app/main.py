from fastapi import FastAPI
from . import models
from .db import engine


models.Base.metadata.create_all(bind=engine)
app = FastAPI()