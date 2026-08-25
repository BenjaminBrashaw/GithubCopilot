from src.app import activities


REQUIRED_FIELDS = {"description", "schedule", "max_participants", "participants"}


def test_get_activities_returns_all_activity_details(client):
    # Arrange
    expected_activity_names = set(activities)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert set(response.json()) == expected_activity_names


def test_get_activities_returns_required_fields_and_valid_participants(client):
    # Arrange
    expected_activity_count = len(activities)

    # Act
    response = client.get("/activities")

    # Assert
    payload = response.json()
    assert len(payload) == expected_activity_count
    for details in payload.values():
        assert REQUIRED_FIELDS.issubset(details)
        assert isinstance(details["participants"], list)
        assert details["max_participants"] >= len(details["participants"])
