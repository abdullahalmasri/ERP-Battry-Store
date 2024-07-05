from models.user import User


class UserController:
    def __init__(self):
        self.users = {}  # A dictionary to store user instances by username

    def add_user(self, user_id, username, password, role):
        if username in self.users:
            raise ValueError(f"User with username '{username}' already exists.")
        self.users[username] = User(user_id, username, password, role)

    def login_user(self, username, password):
        user = self.users.get(username)
        if user and user.verify_password(password):
            return f"Login successful for {username}."
        return "Invalid username or password."

    def logout_user(self, username):
        if username in self.users:
            return f"User {username} logged out successfully."
        return "User not found."
