from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(self, user_id, username, password, role):
        self.user_id = user_id
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.role = role

    def login(self, username, password):
        if self.username == username and self.password == password:
            return f"Login successful! Welcome, {self.username}."
        else:
            return "Login failed. Please check your username and password."

    def logout(self):
        return f"User {self.username} logged out."

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def authenticate_user(self, username, password):
        for user in self.users:
            if user.username == username and user.check_password(password):
                return user
        return None