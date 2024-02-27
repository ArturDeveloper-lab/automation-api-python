import time

import requests

from api_approch_1.api_utils.api import FakeRESTApif, Activiti

fake_rest_api = FakeRESTApif()


def test_create_activiti():
    activiti = Activiti()
    res = fake_rest_api.create_activiti(activiti)
    assert res["id"] == activiti.id
    assert res["title"] == activiti.title
    assert res["completed"] == activiti.completed


def test_create_activiti_part_fields():
    data = {"id": 2}
    res = fake_rest_api.create_activiti(data)
    assert res["id"] == data["id"]


def test_get_activiti():
    fake_rest_api.get_activiti(activiti_id=5)


def test_full_flow_of_activities():
    activiti = Activiti()
    res = fake_rest_api.create_activiti(activiti)
    activiti_update = Activiti(id=1000)
    data = {"id": 10000}
    res = fake_rest_api.update_activiti(res["id"], payload_activiti=data)
    assert res["id"] == data["id"]
    res = fake_rest_api.delete_activiti(res["id"])
    assert res.status_code == 200
