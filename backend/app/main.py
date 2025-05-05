"""
Main module backend.app.main: run the app
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import __title__
from .routes import router

# Init app and configure CORS (required for Swift/iOS)
app = FastAPI(title=__title__)
app.add_middleware(
    CORSMiddleware,
    # TODO: add path to API once deployed in render
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
