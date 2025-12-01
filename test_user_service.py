import pytest

from user_service import UserService, UserNotFound


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


# Итерация 4: список всех пользователей
def test_list_users_returns_all_users():
    service = UserService()
    u1 = service.create_user("A", "a@example.com")
    u2 = service.create_user("B", "b@example.com")

    users = service.list_users()

    assert users == [u1, u2]


# Итерация 5: обновление имени и email
def test_update_user_changes_name_and_email():
    service = UserService()
    user = service.create_user("A", "a@example.com")

    updated = service.update_user(user.id, name="A2", email="a2@example.com")

    assert updated.id == user.id
    assert updated.name == "A2"
    assert updated.email == "a2@example.com"

    assert service.get_user(user.id) == updated


# Итерация 6: обновление только имени
def test_update_user_can_change_only_name():
    service = UserService()
    user = service.create_user("A", "a@example.com")

    updated = service.update_user(user.id, name="A2")

    assert updated.name == "A2"
    assert updated.email == "a@example.com"