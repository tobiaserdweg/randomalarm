"""
Module backend.app.routes: routing functions
"""

import logging

from fastapi import APIRouter

from .logic import simulate_alarm_times, simulate_mult_problem
from .schemas import (
    AlarmResponse,
    AlarmRequest,
    MultProblemRequest,
    MultProblemResponse,
)

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(funcName)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

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

    alarm_datetimes_str = [
        dt.strftime("%Y-%m-%d %H:%M:%S") for dt in alarm_datetimes
    ]
    logger.info(
        f"Request params: method={req.method}, "
        f"start_time={req.start_time}, "
        f"end_time={req.end_time}, "
        f"num_alarms={req.num_alarms}, "
        f"gap_mins={req.gap_mins}. "
        f"Response: alarm_datetimes={alarm_datetimes_str}."
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

    logger.info(
        f"Request params: num_attempts={req.num_attempts}, "
        f"base_difficulty={req.base_difficulty}. "
        f"Response: multiplicators={multiplicators}."
    )
    return MultProblemResponse(
        value_one=multiplicators[0], value_two=multiplicators[1]
    )
