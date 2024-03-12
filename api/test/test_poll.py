from prisma.models import Poll


def test_can_create_poll(client, poll_data, auth):
    response = client.post("/polls", json=poll_data, headers=auth)
    assert response.status_code == 201
    db_poll = Poll.prisma().find_unique(where={"id": response.json["id"]})
    assert db_poll.title == poll_data["title"]


def test_can_find_poll_by_id(client, poll):
    response = client.get(f"/polls/{poll.id}")
    assert response.status_code == 200
    assert "id" in response.json
    assert "title" in response.json


def test_can_update_poll(client, poll, auth):
    patched = {"title": "test-title"}
    response = client.patch(f"/polls/{poll.id}", json=patched, headers=auth)
    assert response.status_code == 201
    assert response.json["title"] == patched["title"]
    assert Poll.prisma().find_unique(where={"id": poll.id}).title == patched["title"]


def test_can_delete_poll(client, poll, auth):
    response = client.delete(f"/polls/{poll.id}", headers=auth)
    assert response.status_code == 204
    db_poll = Poll.prisma().find_unique(where={"id": poll.id})
    assert db_poll is None


def test_unprotected_routes_work_without_auth(client, poll):
    response = client.get("/polls")
    assert response.status_code == 200
    assert len(response.json) == 1
    for poll_json in response.json:
        assert poll.id == poll_json["id"]
    response = client.get(f"/polls/{poll.id}")
    assert response.status_code == 200
    assert poll.id == response.json["id"]


def test_protected_routes_return_error_without_auth(client, poll, poll_data):
    response = client.post("/polls", json=poll_data)
    assert response.status_code == 401
    response = client.patch(f"/polls/{poll.id}", json={"title": "test-title"})
    assert response.status_code == 401
    response = client.delete(f"/polls/{poll.id}")
    assert response.status_code == 401
