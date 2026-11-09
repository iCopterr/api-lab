
import pytest


@pytest.mark.parametrize("excluded", [
    ["Knife"],
    ["Scissors"],
])
def test_excluded_tools(api, auth, excluded):
    res = api.post(
        "/api/pizza",
        json={"excludedTools": excluded},
        headers=auth,
    )

    assert res.status_code == 200
    assert res.json()["pizza"]["tool"] not in excluded
    
    
@pytest.mark.parametrize("excluded", [
    [],
    ["Knife", "Scissors"],
])
def test_other_excluded_tool_partitions(api, auth, excluded):
    res = api.post(
        "/api/pizza",
        json={"excludedTools": excluded},
        headers=auth,
    )

    assert res.status_code == 200
    assert res.json()["pizza"]["tool"] not in excluded


@pytest.mark.xfail(
    strict=True,
    reason="API returns 500 instead of a client error when all tools are excluded",
)
def test_all_tools_excluded(api, auth):
    res = api.post(
        "/api/pizza",
        json={
            "excludedTools": [
                "Knife",
                "Pizza cutter",
                "Scissors",
            ]
        },
        headers=auth,
    )

    assert res.status_code == 400
    assert "error" in res.json()
