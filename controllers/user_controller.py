from models.user import User


class UserController:
    def __init__(self):
        self.users = [
            User(1, "admin", "admin123", "admin"),
            User(2, "john_doe", "password456", "user")
        ]

    def add_user(self, user_id, username, password, role):
        if username in self.users:
            raise ValueError(f"User with username '{username}' already exists.")
        self.users.append(User(user_id, username, password, role))

    # def login_user(self, username, password):
    #     user = self.users.get(username)
    #     if user and user.verify_password(password):
    #         return f"Login successful for {username}."
    #     return "Invalid username or password."

    def logout_user(self, username):
        if username in self.users:
            return f"User {username} logged out successfully."
        return "User not found."

    def authenticate_user(self, username, password):
        for user in self.users:
            if user.username == username and user.check_password(password):
                return user
        return None