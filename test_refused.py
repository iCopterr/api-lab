
import uuid


# A username that already exists cannot be registered again.
def test_duplicate_username_is_refused(api):
    name = "lab-" + uuid.uuid4().hex[:12]
    user = {"username": name, "password": "Pizza-2026"}

    first = api.post("/api/users", json=user)
    assert first.status_code == 201

    second = api.post("/api/users", json=user)
    assert second.status_code == 400
    assert second.json() == {"error": "username already taken"}


# A user cannot log in with an incorrect password.
def test_wrong_password_is_refused(api):
    name = "lab-" + uuid.uuid4().hex[:12]
    user = {"username": name, "password": "Pizza-2026"}

    created = api.post("/api/users", json=user)
    assert created.status_code == 201

    wrong = {"username": name, "password": "WrongPassword"}
    res = api.post("/api/users/token/login", json=wrong)

    assert res.status_code == 401
    assert res.json() == {"error": "authentication failed"}


# A username cannot be empty.
def test_empty_username_is_refused(api):
    user = {"username": "", "password": "Pizza-2026"}

    res = api.post("/api/users", json=user)

    assert res.status_code == 400
    assert res.json() == {"error": "username field is empty"}
