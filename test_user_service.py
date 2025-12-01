# Итерация 1: создание пользователя
def test_create_user_returns_user_with_id():
    service = UserService()

    user = service.create_user(name="Test", email="test@example.com")

    assert user.id == 1
    assert user.name == "Test"
    assert user.email == "test@example.com"
