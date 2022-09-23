import pytest
from src.utils.dict_value_injector import inject_value

def test_inject_value_right_path():
    data = {"a": [23, 24, 25]}
    path = ["a", 3]
    value = 26
    expected_output = {"a": [23, 24, 25, 26]}

    inject_value(data, path, value)

    assert expected_output == data


def test_inject_value_wrong_path():
    data = {"a": [23, 24, 25]}
    path = ["b", 3]
    value = 26

    with pytest.raises(KeyError):
        inject_value(data, path, value)
