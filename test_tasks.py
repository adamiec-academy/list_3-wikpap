import pytest
from test_data import GET_PERFECT_NUMBERS_DATA, FIBONACCI_SEQUENCE_DATA, TOWER_DATA, TOWERS_DATA


def _data_args(data):
    if not data:
        return
    size = len(data[0])
    names = []
    for entry in data:
        name = []
        for arg in range(size - 1):
            name.append(str(entry[arg]))
        names.append(", ".join(name))
    return names


@pytest.mark.parametrize("arg, expected_output", GET_PERFECT_NUMBERS_DATA, ids=_data_args(GET_PERFECT_NUMBERS_DATA))
def test_task_1_get_perfect_numbers(arg, expected_output):
    from task_1 import get_perfect_numbers
    assert get_perfect_numbers(arg) == expected_output


@pytest.mark.parametrize("arg, expected_output", FIBONACCI_SEQUENCE_DATA, ids=_data_args(FIBONACCI_SEQUENCE_DATA))
def test_task_2_fibonacci_sequence(arg, expected_output):
    from task_2 import fibonacci_sequence
    assert fibonacci_sequence(arg) == expected_output


def test_task_3_mountains():
    file = open("task_3.py", "r", encoding="utf-8")
    assert file.readline() != "# Remove this comment to confirm that this task is done"


@pytest.mark.parametrize("n, expected_output", TOWER_DATA, ids=_data_args(TOWER_DATA))
def test_task_4_tower(capfd, n, expected_output):
    with capfd.disabled():
        from task_4 import tower
    tower(n)
    out, _ = capfd.readouterr()
    assert out == expected_output


@pytest.mark.parametrize("data, expected_output", TOWERS_DATA, ids=_data_args(TOWERS_DATA))
def test_task_4_towers(capfd, data, expected_output):
    with capfd.disabled():
        from task_4 import towers
    towers(data)
    out, _ = capfd.readouterr()
    assert out == expected_output


def test_task_5_stars():
    file = open("task_5.py", "r", encoding="utf-8")
    assert file.readline() != "# Remove this comment to confirm that this task is done"
