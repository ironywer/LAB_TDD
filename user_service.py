class UserNotFound(Exception):
    """Пользователь с таким id не найден."""

class UserService:
    def __init__(self):
        self._last_user = None
        self.users = []

    def create_user(self, name, email):
        user = type("User", (), {})()
        user.id = 1
        user.name = name
        user.email = email

        self._last_user = user
        self.users.append(user)
        return user

    def get_user(self, user_id):
        if self._last_user is None:
            raise UserNotFound(f"User with id={user_id} not found")
        return self._last_user

    def list_users(self):
        return self.users

    def update_user(self, id, name, email=None):
        for user in self.users:
            if user.id == id:
                user.name = name
                if email:
                    user.email = email
                return user
        raise UserNotFound(f"User with id={id} not found")