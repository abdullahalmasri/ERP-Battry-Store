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

def render_all_reports(reports):
    report_list = "".join([f"<li>{report.report_id} - {report.report_type}</li>" for report in reports])
    return f"""
    <html>
    <head><title>All Reports</title></head>
    <body>
        <h1>All Reports</h1>
        <ul>{report_list}</ul>
    </body>
    </html>
    """
