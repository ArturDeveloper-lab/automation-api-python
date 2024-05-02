import requests
from course_SolveMe_youtube.configuration import SERVICE_URL_2
from course_SolveMe_youtube.infra.baseclasses.response import Response

resp = requests.get(SERVICE_URL_2)
print(resp)

def test_getting_user_list():
    response =requests.get(SERVICE_URL_2)
    test_obj = Response(response)

def test_somthing(get_number):
    assert 1==1
    print(get_number)