from .utils import client, db_session
import pytest

def test_create_and_get_article(client, db_session):
    # register
    resp = client.post("/auth/register", json={"username": "alice", "email": "a@x.com", "password": "pass"})
    assert resp.status_code == 200
    # login
    resp = client.post("/auth/login", json={"username": "alice", "email": "a@x.com", "password": "pass"})
    token = resp.json()["access_token"]
    headers = {"token": token}
    # create article
    resp = client.post("/articles/", json={"title": "Hello", "content": "World"}, headers=headers)
    assert resp.status_code == 200
    art = resp.json()
    # get article
    resp = client.get(f"/articles/{art['id']}", headers=headers)
    assert resp.status_code == 200
    assert resp.json()["title"] == "Hello"
