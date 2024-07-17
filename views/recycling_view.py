from flask import render_template


def render_process_details(process):
    return f"""
    <html>
    <head><title>Process Details</title></head>
    <body>
        <h1>Process ID: {process.process_id}</h1>
        <p>Battery ID: {process.battery_id}</p>
        <p>Start Date: {process.start_date}</p>
        <p>End Date: {process.end_date}</p>
        <p>Status: {process.status}</p>
    </body>
    </html>
    """


def render_all_processes(user, processes, username):
    return render_template('recycling_template.html', user=user, processes=processes, username=username)
