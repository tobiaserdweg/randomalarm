"""
Unit test for functions in files in app
"""

from datetime import time

import pytest
from app.logic import simulate_alarm_times


@pytest.mark.parametrize(
    "method,start,end,num_alarms,gap_mins,times",
    [
        # Time period shorter than gap_mins
        (
            "linear",
            time(hour=6, minute=30, second=0),
            time(hour=6, minute=30, second=30),
            2,
            1,
            [time(hour=6, minute=30, second=30)],
        ),
        (
            "random",
            time(hour=6, minute=0, second=0),
            time(hour=7, minute=0, second=0),
            2,
            90,
            [time(hour=7, minute=0, second=0)],
        ),
        (
            "linear",
            time(hour=7, minute=0, second=0),
            time(hour=8, minute=0, second=0),
            1,
            75,
            [time(hour=8, minute=0, second=0)],
        ),
        # Too many alarms
        (
            "linear",
            time(hour=10, minute=0, second=0),
            time(hour=10, minute=3, second=0),
            4,
            1,
            [
                time(hour=10, minute=1, second=0),
                time(hour=10, minute=2, second=0),
                time(hour=10, minute=3, second=0),
            ],
        ),
        (
            "linear",
            time(hour=10, minute=0, second=0),
            time(hour=12, minute=0, second=0),
            5,
            30,
            [
                time(hour=10, minute=30, second=0),
                time(hour=11, minute=0, second=0),
                time(hour=11, minute=30, second=0),
                time(hour=12, minute=0, second=0),
            ],
        ),
    ],
)
def test_simulate_alarm_times_backups(
    method, start, end, num_alarms, gap_mins, times
):
    """Test the function app.logic.simulate_alarm_times (back up cases)"""
    alarms_datetimes = simulate_alarm_times(
        method, start, end, num_alarms, gap_mins
    )
    alarms_times = [alarm.time() for alarm in alarms_datetimes]
    assert alarms_times == times


@pytest.mark.parametrize(
    "method,start,end,num_alarms,gap_mins,times",
    [
        (
            "linear",
            time(hour=22, minute=30, second=0),
            time(hour=6, minute=30, second=0),
            4,
            1,
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
            5,
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
            20,
            [
                time(hour=15, minute=29, second=0),
                time(hour=16, minute=45, second=0),
                time(hour=18, minute=1, second=0),
            ],
        ),
    ],
)
def test_simulate_alarm_times_linear(
    method, start, end, num_alarms, gap_mins, times
):
    """Test the function app.logic.simulate_alarm_times (linear mode)"""
    alarms_datetimes = simulate_alarm_times(
        method, start, end, num_alarms, gap_mins
    )
    alarms_times = [alarm.time() for alarm in alarms_datetimes]
    assert alarms_times == times


@pytest.mark.parametrize(
    "start_time,end_time,num_alarms,gap_mins",
    [
        (time(hour=8, minute=0), time(hour=22, minute=0), 10, 30),
    ],
)
def test_simulate_alarm_times_random(
    start_time, end_time, num_alarms, gap_mins
):
    """Test the function app.logic.simulate_alarm_times (random mode)"""
    for _ in range(10000):
        alarms_datetimes = simulate_alarm_times(
            method="random",
            start_time=start_time,
            end_time=end_time,
            num_alarms=num_alarms,
            gap_mins=gap_mins,
        )

        for t1, t2 in zip(alarms_datetimes, alarms_datetimes[1:]):
            assert t1 < t2, f"Test error: {t2} is not later than {t1}."
        assert alarms_datetimes[0].time() >= start_time
        assert alarms_datetimes[num_alarms - 1].time() <= end_time
