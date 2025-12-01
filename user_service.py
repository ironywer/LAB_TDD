class UserService:
    def create_user(self, name, email):
        user = type("User", (), {})()
        user.id = 1
        user.name = name
        user.email = email
        return user