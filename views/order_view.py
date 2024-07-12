def render_order_details(order):
    return f"""
    <html>
    <head><title>Order Details</title></head>
    <body>
        <h1>Order ID: {order.order_id}</h1>
        <p>Battery ID: {order.battery_id}</p>
        <p>Supplier ID: {order.supplier_id}</p>
        <p>Order Date: {order.order_date}</p>
        <p>Delivery Date: {order.delivery_date}</p>
        <p>Status: {order.status}</p>
    </body>
    </html>
    """

def render_all_orders(orders):
    order_list = "".join([f"<li>{order.order_id} - {order.status}</li>" for order in orders])
    return f"""
    <html>
    <head><title>All Orders</title></head>
    <body>
        <h1>All Orders</h1>
        <ul>{order_list}</ul>
    </body>
    </html>
    """
