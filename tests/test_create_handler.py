async def test_create_new_post(client,
                               get_post_from_db):
    text = "testing_test"
    response = client.post(f"/post/new?text={text}")
    data_from_resp = response.json()
    assert response.status_code == 200
    assert data_from_resp["text"] == text
    data_from_db = await get_post_from_db(text)
    assert len(data_from_db) == 1
    post_from_db = dict(data_from_db[0])
    assert str(post_from_db["id"]) == data_from_resp["uuid"]
    assert post_from_db["text"] == data_from_resp["text"]







