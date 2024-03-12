import pytest
import requests

from course_SolveMe_youtube.configuration import SERVICE_URL_2


@pytest.fixture
def get_users():
    response = requests.get(SERVICE_URL_2)
    return response
