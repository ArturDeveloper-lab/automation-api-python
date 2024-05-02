import pytest
import requests

from course_SolveMe_youtube.configuration import service_url, SERVICE_URL_2
from course_SolveMe_youtube.infra.baseclasses.response import Response
from course_SolveMe_youtube.infra.pydantic_schemas.posts import Post
from course_SolveMe_youtube.infra.pydantic_schemas.user import User
from course_SolveMe_youtube.infra.json_schemas.posts import POST_SCHEMA


def test_get_data_with_json_validator():
    r = requests.get(service_url)
    response = Response(r)
    response.assert_status_code(200).validate_for_json_validator(POST_SCHEMA)


def test_get_data_with_pydantic_validator():
    r = requests.get(service_url)
    response = Response(r)
    response.assert_status_code(200).validate_for_pydentic_validator(Post)


def test_getting_user_list(get_users, calculate, make_number):
    Response(get_users).assert_status_code(200).validate_for_pydentic_validator(User)
    # print(calculate)
    # print(f" aaafff {calculate(1,1)}")
    # print(make_number)

@pytest.mark.prodaction
@pytest.mark.skip("issue with network connection")
def test_another():
    assert 1 == 1


@pytest.mark.development
@pytest.mark.parametrize("first_value,second_value,result", [
    (1, 2, 3),
    (-1, -2, -3),
    (-1, 2, 1),
    ("b", -2, None),
    ("b", "b", None)
])
def test_calculator(first_value, second_value, result, calculate):
    assert calculate(first_value, second_value) == result
