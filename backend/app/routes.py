"""
Module backend.api.routes: routing functions
"""

from fastapi import APIRouter

from .logic import simulate_alarm_times
from .schemas import AlarmResponse, AlarmRequest

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
    )
    return AlarmResponse(alarms=alarm_datetimes)
