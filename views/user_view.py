# views/user_view.py
from flask import render_template

def render_login_view(error=None):
    return render_template('user_login.html', error=error)

def render_dashboard_view(username, message):
    return render_template('user_dashboard.html', username=username, message=message)
