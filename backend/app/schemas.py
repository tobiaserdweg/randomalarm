"""
Module backend.api.schemas: definition of schemata
"""

from datetime import time, datetime
from typing import Literal

from pydantic import BaseModel, Field


class AlarmRequest(BaseModel):
    method: Literal["random", "linear"]
    start_time: time
    end_time: time
    num_alarms: int = Field(..., ge=0)


class AlarmResponse(BaseModel):
    alarms: list[datetime]
