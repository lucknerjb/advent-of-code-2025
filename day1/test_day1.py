import pytest
from .main import _perform_single_rotation


def test_day1_partial_rotation_right():
    start = 50
    operation = "R48"
    expected_dial_number = 98
    assert _perform_single_rotation(start, int(operation[1:])) == expected_dial_number


def test_day1_partial_rotation_left():
    start = 50
    operation = "L5"
    expected_dial_number = 55
    assert _perform_single_rotation(start, int(operation[1:])) == expected_dial_number


def test_day1_full_rotation_right():
    start = 50
    operation = "R168"
    expected_dial_number = 18
    assert _perform_single_rotation(start, int(operation[1:])) == expected_dial_number