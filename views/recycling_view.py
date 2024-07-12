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

def render_all_processes(processes):
    process_list = "".join([f"<li>{process.process_id} - {process.status}</li>" for process in processes])
    return f"""
    <html>
    <head><title>All Processes</title></head>
    <body>
        <h1>All Processes</h1>
        <ul>{process_list}</ul>
    </body>
    </html>
    """
