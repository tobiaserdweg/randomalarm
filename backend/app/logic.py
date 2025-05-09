"""
Module backend.app.logic: implementation of actual functionalities
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
    gap_mins: int,
) -> list[datetime]:
    """
    Derive the times at which the alarm is triggered by the app. If method is
    linear, then the alarm times are equally distributed over to given time
    interval. Otherwise, the times are sampled randomly. The alarm is triggered
    no more than once every gap_mins minutes.

    :param method: method to derive alarm times
    :param start_time: start of the time slot
    :param end_time: start of the time slot
    :param num_alarms: number of alarams to be generated
    :param gap_mins: minimal time gap between alarms (in minutes)
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
    if num_alarms > total_minutes / gap_mins:
        num_alarms = math.floor(total_minutes / gap_mins)

    # In case the time slot is too short, only one alarm time is triggered
    if method not in ["linear", "random"]:
        raise ValueError(
            f"Invalid parameter passed to function "
            f"backend.app.logic.simulate_alarm_times: method = {method}"
        )
    else:
        if start_datetime + timedelta(minutes=gap_mins) > end_datetime:
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
                shifts = np.sort(
                    np.random.uniform(0, total_seconds, size=num_alarms)
                )
                alarm_datetimes = [
                    start_datetime + timedelta(seconds=math.floor(shift))
                    for shift in shifts
                ]

                for k in range(1, num_alarms, 1):
                    delta = (
                        alarm_datetimes[k] - alarm_datetimes[k - 1]
                    ).total_seconds()
                    if delta <= gap_mins * 60:
                        shift = timedelta(seconds=gap_mins * 60 - delta)
                        for j in range(k, num_alarms, 1):
                            alarm_datetimes[j] += shift

                # Cap and derivation of unique values
                alarm_datetimes = [
                    min(alarm, end_datetime) for alarm in alarm_datetimes
                ]
                alarm_datetimes = sorted(list(set(alarm_datetimes)))
                return alarm_datetimes


def simulate_mult_problem(
    num_attempts: int, base_difficulty: Literal["easy", "moderate", "hard"]
) -> tuple[int, int]:
    """
    Simulate a multiplication problem.

    :param num_attempts: number of previous attempts
    :param base_difficulty: base difficulty
    :return: list of two integers to be multiplied
    """
    difficulty_dict = {"easy": 1, "moderate": 2, "hard": 3}
    difficulty_int = difficulty_dict[base_difficulty]

    # Derive difficulty to be applied
    if difficulty_int == 1:
        adjustment = (
            2 if num_attempts >= 3 else 1 if num_attempts in (1, 2) else 0
        )
    else:
        adjustment = 1 if num_attempts >= 2 else 0
    difficulty_int = min(3, difficulty_int + adjustment)

    low, high = {1: (2, 13), 2: (5, 26), 3: (20, 101)}[difficulty_int]
    return tuple(np.random.randint(low=low, high=high, size=2).tolist())
