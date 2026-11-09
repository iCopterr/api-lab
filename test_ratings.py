
# A logged-in user can create a rating for a pizza.
def test_create_rating(api, auth, pizza_id):
    data = {"pizza_id": pizza_id, "stars": 5}
    res = api.post("/api/ratings", json=data, headers=auth)

    assert res.status_code == 201

    body = res.json()
    assert body["pizza_id"] == pizza_id
    assert body["stars"] == 5
    assert isinstance(body["id"], int)


# A user can read a rating they created.
def test_read_rating(api, auth, rating):
    res = api.get("/api/ratings/" + str(rating["id"]), headers=auth)
    assert res.status_code == 200
    assert res.json()["id"] == rating["id"]
    assert res.json()["stars"] == 3


# A user can update a rating they created.
def test_update_rating(api, auth, rating):
    res = api.put(
        "/api/ratings/" + str(rating["id"]),
        json={"stars": 5},
        headers=auth,
    )
    assert res.status_code == 200
    assert res.json()["stars"] == 5


# A user can delete a rating they created.
def test_delete_rating(api, auth, rating):
    res = api.delete("/api/ratings/" + str(rating["id"]), headers=auth)
    assert res.status_code == 204
