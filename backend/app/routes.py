"""
Main module backend\\api\\routes.py: routing function
"""

from fastapi import APIRouter

router = APIRouter()


@router.post("/")
def say_hello():
    return {"message": "Hello World"}
