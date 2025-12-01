import pytest

from user_service import UserService

# Итерация 1: создание пользователя
def test_create_user_returns_user_with_id():
    service = UserService()

    user = service.create_user(name="Test", email="test@example.com")

    assert user.id == 1
    assert user.name == "Test"
    assert user.email == "test@example.com"


# Итерация 2: созданного пользователя можно прочитать по id
def test_created_users_are_stored_and_can_be_read_by_id():
    service = UserService()
    created = service.create_user("hello", "world@example.com")

    fetched = service.get_user(created.id)

    assert fetched == created


# Итерация 3: запрос несуществующего пользователя -> исключение
def test_get_user_raises_for_unknown_id():
    service = UserService()

    with pytest.raises(UserNotFound):
        service.get_user(999)
