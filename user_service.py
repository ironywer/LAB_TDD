class UserNotFound(Exception):
    """Пользователь с таким id не найден."""

class UserService:
    def __init__(self):
        self._last_user = None

    def create_user(self, name, email):
        user = type("User", (), {})()
        user.id = 1
        user.name = name
        user.email = email

        self._last_user = user
        return user

    def get_user(self, user_id):
        if self._last_user is None:
            raise UserNotFound(f"User with id={user_id} not found")
        return self._last_user