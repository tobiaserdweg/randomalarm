"""
Main module backend.app.main: run the app
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import __title__
from .routes import router

# Init app and configure CORS (required for Swift/iOS)
# TODO: how to import name from pyproject.toml file
app = FastAPI(title=__title__)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://randomalarm.onrender.com/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
