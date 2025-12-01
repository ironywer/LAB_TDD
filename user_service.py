class UserNotFound(Exception):
    """Пользователь с таким id не найден."""

class InvalidUserData(Exception):
    """Переданы некорректные данные пользователя."""

class UserService:
    def __init__(self):
        self.users = []

    def create_user(self, name, email):
        if name == '' or '@' not in email:
            raise InvalidUserData
        user = type("User", (), {})()
        user.id = 1
        user.name = name
        user.email = email

        self.users.append(user)
        return user

    def get_user(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user
        raise UserNotFound(f"User with id={user_id} not found")

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

    def delete_user(self, id):
        for i in range(len(self.users)):
            if self.users[i].id == id:
                self.users.pop(i)