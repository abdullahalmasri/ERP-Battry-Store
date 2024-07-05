class User:
    def __init__(self, user_id, username, password, role):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role

    def login(self, username, password):
        if self.username == username and self.password == password:
            return f"Login successful! Welcome, {self.username}."
        else:
            return "Login failed. Please check your username and password."

    def logout(self):
        return f"User {self.username} logged out."

    def verify_password(self, password):
        # Simple password comparison (for demonstration purposes only)
        return self.password == password
