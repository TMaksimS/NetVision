import uuid

from fastapi.testclient import TestClient
from pytest import fixture


async def test_get_count_handler(
        client: TestClient,
        create_post_in_db: fixture
):
    count = 3
    for i in range(count):
        post_id = uuid.uuid4()
        await create_post_in_db(post_id, "Counter post")

    response = client.get(f"/post/all/{count}")
    assert response.status_code == 200

    resp_data = response.json()
    assert len(resp_data) == 3