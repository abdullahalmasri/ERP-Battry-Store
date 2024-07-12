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

def render_all_suppliers(suppliers):
    supplier_list = "".join([f"<li>{supplier.supplier_id} - {supplier.name}</li>" for supplier in suppliers])
    return f"""
    <html>
    <head><title>All Suppliers</title></head>
    <body>
        <h1>All Suppliers</h1>
        <ul>{supplier_list}</ul>
    </body>
    </html>
    """
