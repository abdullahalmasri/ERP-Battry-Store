from flask import render_template


def render_report_details(report):
    return f"""
    <html>
    <head><title>Report Details</title></head>
    <body>
        <h1>Report ID: {report.report_id}</h1>
        <p>Type: {report.report_type}</p>
        <p>Generated Date: {report.generated_date}</p>
        <p>Data: {report.data}</p>
    </body>
    </html>
    """

def render_all_reports(user, reports, username):
    return render_template("report_template.html", user=user, reports=reports, username=username)
