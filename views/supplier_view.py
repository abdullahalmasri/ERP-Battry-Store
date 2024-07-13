from flask import render_template


def render_supplier_details(supplier):
    return f"""
    <html>
    <head><title>Supplier Details</title></head>
    <body>
        <h1>Supplier ID: {supplier.supplier_id}</h1>
        <p>Name: {supplier.name}</p>
        <p>Contact Info: {supplier.contact_info}</p>
        <p>Performance Rating: {supplier.performance_rating}</p>
    </body>
    </html>
    """


def render_all_suppliers(suppliers, username):
    return render_template('supplier_template.html', suppliers=suppliers, username=username)
