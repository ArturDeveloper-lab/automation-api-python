from random import randrange

import pytest


@pytest.fixture
def get_number():
    return randrange(1, 1000, 5)


def _calculator(a, b):
    if isinstance(a,int) and isinstance(b,int):
        return a + b
    else:
        return None


@pytest.fixture
def calculate():
    return _calculator


@pytest.fixture
def make_number():
    print("i am getting number")
    number = randrange(1, 1000, 5)
    yield number
    print(f"Number at  home {number}")
