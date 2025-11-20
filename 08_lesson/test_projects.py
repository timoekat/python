import requests
from config import (
    BASE_URL,
    HEADERS,
    PROJECT_ID,
    PROJECT_TITLE,
    UPDATED_PROJECT_TITLE
)


def test_get_positive():
    resp = requests.get(f"{BASE_URL}projects/{PROJECT_ID}", headers=HEADERS)
    print(resp.text)
    assert resp.status_code == 200
    assert "title" in resp.json()


def test_get_negative_invalid_id():
    invalid_id = "invalid-id"
    resp = requests.get(f"{BASE_URL}projects/{invalid_id}", headers=HEADERS)
    print(resp.text)
    assert resp.status_code == 404


def test_post():
    payload = {"title": PROJECT_TITLE}
    resp = requests.post(f"{BASE_URL}projects", headers=HEADERS, json=payload)
    print(resp.text)
    assert resp.status_code == 201


def test_post_negative():
    payload = {}
    resp = requests.post(f"{BASE_URL}projects", headers=HEADERS, json=payload)
    print(resp.text)
    assert resp.status_code == 400
    assert "title should not be empty" in resp.text


def test_put_positive():
    payload = {"title": UPDATED_PROJECT_TITLE}
    resp = requests.put(f"{BASE_URL}projects/{PROJECT_ID}",
                        headers=HEADERS, json=payload)
    print(resp.text)
    assert resp.status_code == 200


def test_put_negative_empty_title():
    payload = {"title": ""}
    resp = requests.put(f"{BASE_URL}projects/{PROJECT_ID}",
                        headers=HEADERS, json=payload)
    print(resp.text)
    assert resp.status_code == 400
    assert "title should not be empty" in resp.text
