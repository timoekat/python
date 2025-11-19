import os
import requests

base_url = "https://ru.yougile.com/api-v2/"


API_KEY = os.getenv("YOUGILE_API_KEY")

headers = {
    "Authorization": f"Bearer {API_KEY}"
}


def test_put_positive():
    project_id = "09c0a97d-9bd3-4227-ab80-d4ba82f3c4bf"
    payload = {"title": "UpdatedProjectTitle"}

    resp = requests.put(f"{base_url}projects/{project_id}",
                        headers=headers, json=payload)
    print(resp.text)
    assert resp.status_code == 200


def test_put_negative_empty_title():
    project_id = "09c0a97d-9bd3-4227-ab80-d4ba82f3c4bf"
    payload = {"title": ""}

    resp = requests.put(f"{base_url}projects/{project_id}",
                        headers=headers, json=payload)
    print(resp.text)
    assert resp.status_code == 400
    assert "title should not be empty" in resp.text
