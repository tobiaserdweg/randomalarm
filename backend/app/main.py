"""
Main module backend.app.main: run the app
"""

from importlib.metadata import metadata

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import router

project_metadata = metadata("backend")
project_name = project_metadata["Name"]

# Init app and configure CORS (required for Swift/iOS)
app = FastAPI(title=project_name)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://randomalarm.onrender.com/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
