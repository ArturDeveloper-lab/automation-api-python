import requests

head = {
    "Accept": "text/plan"
}

response = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/5",headers=head)
print(response.status_code)
print(response.json())
