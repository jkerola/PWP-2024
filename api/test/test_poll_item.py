from prisma.models import PollItem


def test_can_create_poll_item(client, auth, poll_item_data):
    response = client.post("/pollitems", json=poll_item_data, headers=auth)
    assert response.status_code == 201
    item = PollItem.prisma().find_unique(where={"id": response.json["id"]})
    assert item is not None
    assert item.description == poll_item_data["description"]


def test_can_vote_poll_item(client, poll_item):
    assert poll_item.votes == 0
    response = client.post(
        f"/pollitems/{poll_item.id}",
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 201
    assert PollItem.prisma().find_unique(where={"id": poll_item.id}).votes == 1


def test_can_patch_poll_item(client, poll_item, poll_item_data, auth):
    patched = {
        **poll_item_data,
        "description": "test-description",
    }
    response = client.patch(
        f"/pollitems/{poll_item.id}",
        json=patched,
        headers=auth,
    )
    assert response.status_code == 200
    db_poll_item = PollItem.prisma().find_unique({"id": poll_item.id})
    assert db_poll_item is not None
    assert db_poll_item.description == patched["description"]


def test_can_delete_poll_item(client, poll_item, auth):
    response = client.delete(f"/pollitems/{poll_item.id}", headers=auth)
    assert response.status_code == 200
    assert PollItem.prisma().find_unique({"id": poll_item.id}) is None


def test_protected_routes_are_protected(client, poll_item_data, poll_item, auth):
    response = client.post(
        "/pollitems",
        json=poll_item_data,
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 401
    response = client.patch(
        f"/pollitems/{poll_item.id}",
        json={"description": "test-description"},
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 401
    response = client.delete(
        f"/pollitems/{poll_item.id}",
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 401
