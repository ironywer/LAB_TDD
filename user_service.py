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
        return self._last_user