
# A logged-in user can create a rating for a pizza.
def test_create_rating(api, auth, pizza_id):
    data = {"pizza_id": pizza_id, "stars": 5}
    res = api.post("/api/ratings", json=data, headers=auth)

    assert res.status_code == 201

    body = res.json()
    assert body["pizza_id"] == pizza_id
    assert body["stars"] == 5
    assert isinstance(body["id"], int)
