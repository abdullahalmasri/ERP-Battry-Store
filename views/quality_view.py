def render_inspection_details(qc):
    return f"""
    <html>
    <head><title>Inspection Details</title></head>
    <body>
        <h1>QC ID: {qc.qc_id}</h1>
        <p>Battery ID: {qc.battery_id}</p>
        <p>Inspection Date: {qc.inspection_date}</p>
        <p>Results: {qc.results}</p>
        <p>Issues: {qc.issues}</p>
    </body>
    </html>
    """

def render_all_inspections(quality_controls):
    qc_list = "".join([f"<li>{qc.qc_id} - {qc.results}</li>" for qc in quality_controls])
    return f"""
    <html>
    <head><title>All Inspections</title></head>
    <body>
        <h1>All Inspections</h1>
        <ul>{qc_list}</ul>
    </body>
    </html>
    """
