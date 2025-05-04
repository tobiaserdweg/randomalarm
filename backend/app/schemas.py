"""
Module backend.app.schemas: definition of schemata
"""

from datetime import time, datetime
from typing import Literal

from pydantic import BaseModel, Field


class AlarmRequest(BaseModel):
    method: Literal["random", "linear"]
    start_time: time
    end_time: time
    num_alarms: int = Field(..., ge=1)
    gap_mins: int = Field(..., ge=0)


class AlarmResponse(BaseModel):
    alarms: list[datetime]


class MultProblemRequest(BaseModel):
    num_attempts: int = Field(..., ge=0)
    base_difficulty: Literal["easy", "moderate", "hard"]


class MultProblemResponse(BaseModel):
    value_one: int = Field(..., ge=1, le=1000)
    value_two: int = Field(..., ge=1, le=1000)
