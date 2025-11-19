import os
import requests

base_url = "https://ru.yougile.com/api-v2/"


API_KEY = os.getenv("YOUGILE_API_KEY")

headers = {
    "Authorization": f"Bearer {API_KEY}"
}


def test_get_positive():
    project_id = "09c0a97d-9bd3-4227-ab80-d4ba82f3c4bf"

    resp = requests.get(f"{base_url}projects/{project_id}", headers=headers)
    print(resp.text)
    assert resp.status_code == 200
    assert "title" in resp.json()


def test_get_negative_invalid_id():
    project_id = "invalid-id"

    resp = requests.get(f"{base_url}projects/{project_id}", headers=headers)
    print(resp.text)
    assert resp.status_code == 404
