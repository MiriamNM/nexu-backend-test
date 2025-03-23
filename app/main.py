from fastapi import FastAPI
from . import routes
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(routes.router)
