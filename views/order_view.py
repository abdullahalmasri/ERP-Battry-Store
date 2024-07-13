from flask import render_template


def track_order(order):
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


def render_all_orders(orders, username):
    print('order view user ', username)
    return render_template('order_template.html', orders=orders, username=username)
