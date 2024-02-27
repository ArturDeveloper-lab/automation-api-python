import random
import time
from datetime import datetime, timezone
import requests
from faker import Faker

fake = Faker()


class Activiti:
    def __init__(self, id=None, title=None, completed=None):
        self.id = id or random.randint(1, 100)
        self.title = title or fake.text(10)
        self.dueDate = str(datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z')
        self.completed = completed or fake.boolean()


class FakeRESTApif:

    @property
    def __headers(self):
        return {"accept": "text/plain", "Content-Type": "application/json"}

    def request(self, method, rel_url, **kwargs):
        url = f"https://fakerestapi.azurewebsites.net{rel_url}"
        # base_url = "https://fakerestapi.azurewebsites.net"
        # url = urljoin(base_url, rel_url)
        kwargs.update({"headers": self.__headers})
        time.sleep(5)
        res = requests.request(method, url, **kwargs)
        res.raise_for_status()
        return res

    activities_url = "/api/v1/Activities"

    def create_activiti(self, payload_activiti):
        # Check if the payload is already a dictionary
        if isinstance(payload_activiti, dict):
            data_dict = payload_activiti
        else:
            # If it's not a dictionary, assume it's an instance of a class and use vars() to convert
            data_dict = vars(payload_activiti)
        response = self.request("post", rel_url=self.activities_url, json=data_dict)
        print("Create Task Response:", response.json())
        return response.json()

    def get_activiti(self, activiti_id):
        get_task = f"{self.activities_url}/{activiti_id}"
        response = self.request("get", rel_url=get_task)
        return response.json()

    def update_activiti(self, activiti_id, payload_activiti):
        # Check if the payload is already a dictionary
        if isinstance(payload_activiti, dict):
            data_dict = payload_activiti
        else:
            # If it's not a dictionary, assume it's an instance of a class and use vars() to convert
            data_dict = vars(payload_activiti)
        response = self.request("put", f"{self.activities_url}/{activiti_id}", json=data_dict)
        return response.json()

    def delete_activiti(self, activiti_id):
        get_activiti_url = f"{self.activities_url}/{activiti_id}"
        response = self.request("delete", rel_url=get_activiti_url)
        return response
