from random import randrange

import pytest


@pytest.fixture
def get_number():
    return randrange(1, 1000, 5)


def _calculator(a, b):
    return a + b


@pytest.fixture
def calculate():
    return _calculator
