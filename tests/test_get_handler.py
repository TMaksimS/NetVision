import uuid

from fastapi.testclient import TestClient


async def test_get_current_post(client: TestClient, create_post_in_db):
    post_data = {"uuid": uuid.uuid4(),
                 "text": "current_text"}
    await create_post_in_db(post_data["uuid"], post_data["text"])
    response = client.get(f"/post/{post_data['uuid']}")
    assert response.status_code == 200
    resp_data = response.json()
    assert resp_data["uuid"] == str(post_data["uuid"])
    assert resp_data["text"] == post_data["text"]


async def test_get_current_post_invalid(client: TestClient):
    response = client.get(f"/post/{uuid.uuid4()}")
    assert response.status_code == 404



