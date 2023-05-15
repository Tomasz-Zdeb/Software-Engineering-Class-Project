from api.utilities.auth import user_has_permission, hash_password


def test_user_has_permission(client):
    with client.application.app_context():
        assert user_has_permission(1, 1) is True
        assert user_has_permission(1, 2) is False
        assert user_has_permission(2, 1) is False
        assert user_has_permission(None, 1) is False
        assert user_has_permission(1, None) is False


def test_hash_password(client):
    assert hash_password('test_pass') == 'test_pass'
