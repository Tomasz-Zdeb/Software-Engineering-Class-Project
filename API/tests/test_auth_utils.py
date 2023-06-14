from api.utilities.auth import user_has_permission


def test_user_has_permission(client):
    with client.application.app_context():
        assert user_has_permission(1, 1) is True
        assert user_has_permission(1, 2) is True
        assert user_has_permission(1, 3) is False
        assert user_has_permission(2, 1) is False
        assert user_has_permission(None, 1) is False
        assert user_has_permission(1, None) is False
