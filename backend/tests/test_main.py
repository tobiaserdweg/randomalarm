"""
Unit test for functions in files in app
"""

from datetime import time

import pytest

from app.logic import simulate_alarm_times


@pytest.mark.parametrize(
    "method,start,end,num_alarms,times",
    [
        # Time period shorter than 1 minute
        (
            "linear",
            time(hour=6, minute=30, second=0),
            time(hour=6, minute=30, second=30),
            2,
            [time(hour=6, minute=30, second=30)],
        ),
        # Too many alarms
        (
            "linear",
            time(hour=10, minute=0, second=0),
            time(hour=10, minute=3, second=0),
            4,
            [
                time(hour=10, minute=1, second=0),
                time(hour=10, minute=2, second=0),
                time(hour=10, minute=3, second=0),
            ],
        ),
        # General
        (
            "linear",
            time(hour=22, minute=30, second=0),
            time(hour=6, minute=30, second=0),
            4,
            [
                time(hour=0, minute=30, second=0),
                time(hour=2, minute=30, second=0),
                time(hour=4, minute=30, second=0),
                time(hour=6, minute=30, second=0),
            ],
        ),
        (
            "linear",
            time(hour=23, minute=11, second=0),
            time(hour=5, minute=13, second=0),
            7,
            [
                time(hour=0, minute=2, second=0),
                time(hour=0, minute=53, second=0),
                time(hour=1, minute=44, second=0),
                time(hour=2, minute=35, second=0),
                time(hour=3, minute=26, second=0),
                time(hour=4, minute=17, second=0),
                time(hour=5, minute=8, second=0),
            ],
        ),
        (
            "linear",
            time(hour=14, minute=13, second=0),
            time(hour=18, minute=2, second=0),
            3,
            [
                time(hour=15, minute=29, second=0),
                time(hour=16, minute=45, second=0),
                time(hour=18, minute=1, second=0),
            ],
        ),
    ],
)
def test_simulate_alarm_times_linear(method, start, end, num_alarms, times):
    """Test the function app.logic.simulate_alarm_times (linear mode)"""
    alarms_datetimes = simulate_alarm_times(method, start, end, num_alarms)
    alarms_times = [alarm.time() for alarm in alarms_datetimes]
    assert alarms_times == times
