"""
Main module backend.main: run the app
"""

from fastapi import FastAPI

from . import __title__
from .routes import router

app = FastAPI(title=__title__)

app.include_router(router)
