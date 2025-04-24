"""
Main module backend\\api\\routes.py: routing function
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/greetings")
def say_hello():
    return {"message": "Hello World"}
