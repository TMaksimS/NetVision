import uuid

from fastapi.testclient import TestClient


async def test_get_all_post(client: TestClient, create_post_in_db):
    post_data = {"uuid": uuid.uuid4(),
                 "text": "For all posts"}
    await create_post_in_db(post_data["uuid"],
                            post_data["text"])
    response = client.get("/post/all")
    assert response.status_code == 200
    data_resp = response.json()
    assert len(data_resp) != 0
