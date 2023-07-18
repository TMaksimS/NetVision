import uuid

from fastapi.testclient import TestClient
from pytest import fixture


async def test_delete_current_post(
        client: TestClient,
        create_post_in_db: fixture,
        get_post_from_db: fixture
):
    post_data = {
        "uuid": uuid.uuid4(),
        "text": "text_for_deleted"
    }
    await create_post_in_db(post_data["uuid"],
                            post_data["text"])
    response = client.delete(f"/post/{post_data['uuid']}")
    assert response.status_code == 200

    resp_data = response.json()
    assert resp_data["uuid"] == str(post_data["uuid"])
    assert resp_data["message"] == "Post has been deleted"


async def test_delete_incorrect_post(client: TestClient):
    response = client.delete(f"/post/{uuid.uuid4()}")
    assert response.status_code == 404

    resp_data = response.json()
    assert resp_data["detail"]["message"] == "Incorrect request"
