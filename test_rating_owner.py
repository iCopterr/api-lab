
# Another user must not read the owner's rating.
def test_other_user_cannot_read(api, auth, other_auth, rating):
    rating_id = rating["id"]

    res = api.get(
        "/api/ratings/" + str(rating_id),
        headers=other_auth,
    )

    print("Other user GET status:", res.status_code)
    assert 400 <= res.status_code <= 499

    owner_res = api.get(
        "/api/ratings/" + str(rating_id),
        headers=auth,
    )
    assert owner_res.status_code == 200
    assert owner_res.json()["stars"] == 3


# Another user must not update the owner's rating.
def test_other_user_cannot_update(api, auth, other_auth, rating):
    rating_id = rating["id"]

    res = api.put(
        "/api/ratings/" + str(rating_id),
        json={"stars": 5},
        headers=other_auth,
    )

    print("Other user PUT status:", res.status_code)
    assert 400 <= res.status_code <= 499

    owner_res = api.get(
        "/api/ratings/" + str(rating_id),
        headers=auth,
    )
    assert owner_res.status_code == 200
    assert owner_res.json()["stars"] == 3


# Another user must not delete the owner's rating.
def test_other_user_cannot_delete(api, auth, other_auth, rating):
    rating_id = rating["id"]

    res = api.delete(
        "/api/ratings/" + str(rating_id),
        headers=other_auth,
    )

    print("Other user DELETE status:", res.status_code)
    assert 400 <= res.status_code <= 499

    owner_res = api.get(
        "/api/ratings/" + str(rating_id),
        headers=auth,
    )
    assert owner_res.status_code == 200
    assert owner_res.json()["stars"] == 3
