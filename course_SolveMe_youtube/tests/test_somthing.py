import requests

from course_SolveMe_youtube.configuration import service_url
from course_SolveMe_youtube.infra.baseclasses.response import Response
from course_SolveMe_youtube.infra.schemas.posts import POST_SCHEMA


def test_get_data():
    r = requests.get(service_url)
    response = Response(r)
    response.assert_status_code(200).validate(POST_SCHEMA)





