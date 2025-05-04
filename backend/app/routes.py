"""
Module backend.app.routes: routing functions
"""

from fastapi import APIRouter

from .logic import simulate_alarm_times, simulate_mult_problem
from .schemas import (
    AlarmResponse,
    AlarmRequest,
    MultProblemRequest,
    MultProblemResponse,
)

router = APIRouter()


@router.post("/simulate-alarms", response_model=AlarmResponse)
def generate_alarms(req: AlarmRequest) -> AlarmResponse:
    """
    Route function app.logic.simulate_alarm_times

    :param req: AlarmRequest object
    :return: AlarmResponse object
    """
    alarm_datetimes = simulate_alarm_times(
        method=req.method,
        start_time=req.start_time,
        end_time=req.end_time,
        num_alarms=req.num_alarms,
        gap_mins=req.gap_mins,
    )
    return AlarmResponse(alarms=alarm_datetimes)


@router.post("/simulate-multiplication", response_model=MultProblemResponse)
def generate_mult(req: MultProblemRequest) -> MultProblemResponse:
    """
    Route function app.logic.simulate_mult_problem

    :param req: MultProblemRequest object
    :return: MultProblemResponse object
    """
    multiplicators = simulate_mult_problem(
        num_attempts=req.num_attempts, base_difficulty=req.base_difficulty
    )
    return MultProblemResponse(
        value_one=multiplicators[0], value_two=multiplicators[1]
    )
