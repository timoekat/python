import os
import requests

base_url = "https://ru.yougile.com/api-v2/"

API_KEY = os.getenv("YOUGILE_API_KEY")

headers = {
    "Authorization": f"Bearer {API_KEY}"
}


def test_post():
    payload = {
        "title": "EkaterinaT"
    }

    resp = requests.post(base_url + "projects", headers=headers, json=payload)
    print(resp.text)
    assert resp.status_code == 201


def test_post_negative():
    payload = {}
    resp = requests.post(base_url + "projects", headers=headers, json=payload)
    print(resp.text)
    assert resp.status_code == 400
    assert "title should not be empty" in resp.text
