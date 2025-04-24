"""
Module backend.logic: implementation of actual functionalities
"""

import math
from datetime import datetime, time, timedelta
from typing import Literal

import numpy as np


def simulate_alarm_times(
    method: Literal["random", "linear"],
    start_time: time,
    end_time: time,
    num_alarms: int,
) -> list[datetime]:
    """
    Derive the times at which the alarm is triggered by the app. If method is
    linear, then the alarm times are equally distributed over to given time
    interval. Otherwise, the times are sampled randomly. The alarm is triggered
    no more than once every minute.

    :param method: method to derive alarm times
    :param start_time: start of the time slot
    :param end_time: start of the time slot
    :param num_alarms: number of alarams to be generated
    :return: list of datetime.datetime objects
    """
    # Derive start and end time as datetime objects
    today = datetime.today().date()
    start_datetime = datetime.combine(today, start_time)
    end_datetime = datetime.combine(today, end_time)
    if end_datetime <= start_datetime:
        end_datetime += timedelta(days=1)

    total_seconds = (end_datetime - start_datetime).total_seconds()
    total_minutes = int(total_seconds / 60)
    if num_alarms > total_minutes:
        num_alarms = math.floor(total_minutes)

    # In case the time slot is too short, only one alarm time is triggered
    if method not in ["linear", "random"]:
        raise ValueError(
            f"Invalid parameter passed to function "
            f"backend.app.logic.simulate_alarm_times: method = {method}"
        )
    else:
        if start_datetime + timedelta(minutes=1) > end_datetime:
            return [end_datetime]
        else:
            if method == "linear":
                minute_addons = math.floor(
                    total_minutes / num_alarms
                ) * np.arange(1, num_alarms + 1, 1)
                alarm_datetimes = [
                    start_datetime + timedelta(minutes=int(addon))
                    for addon in minute_addons
                ]
                return alarm_datetimes
            else:
                available_seconds = total_seconds - (num_alarms - 1) * 60
                random_addonds = sorted(
                    np.random.uniform(0, available_seconds, num_alarms)
                )
                alarm_datetimes = [
                    start_datetime + timedelta(seconds=addon + k * 60)
                    for k, addon in enumerate(random_addonds)
                ]
                return alarm_datetimes
