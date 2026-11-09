
import pytest


@pytest.mark.parametrize(
    "stars, expected_status",
    [
        (0, 400),
        (1, 200),
        (5, 200),
        (6, 400),
    ],
)
def test_update_rating_boundary(
    api, auth, rating, stars, expected_status
):
    rating_id = rating["id"]

    # Update the rating with the boundary value.
    res = api.put(
        "/api/ratings/" + str(rating_id),
        json={"stars": stars},
        headers=auth,
    )

    assert res.status_code == expected_status

    # Read the rating again to verify its stored value.
    read = api.get(
        "/api/ratings/" + str(rating_id),
        headers=auth,
    )

    assert read.status_code == 200

    if expected_status == 200:
        assert read.json()["stars"] == stars
    else:
        assert read.json()["stars"] == 3
