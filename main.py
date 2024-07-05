from flask import Flask, request, redirect, url_for
from controllers.user_controller import UserController
from views.user_view import render_login_view, render_dashboard_view

app = Flask(__name__, template_folder='views')  # Ensure the template folder is 'views'
user_controller = UserController()

# Add example users
user_controller.add_user(1, "admin", "admin123", "administrator")
user_controller.add_user(2, "john_doe", "password456", "regular")

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        message = user_controller.login_user(username, password)
        if "successful" in message:
            return redirect(url_for('dashboard', username=username))
        else:
            return render_login_view(error=message)
    return render_login_view()

@app.route('/dashboard/<username>')
def dashboard(username):
    message = "You are logged in!"
    return render_dashboard_view(username, message)

@app.route('/logout')
def logout():
    username = request.args.get('username', '')
    logout_message = user_controller.logout_user(username)
    return render_login_view(error=logout_message)

if __name__ == "__main__":
    app.run(debug=True, port=9000)
