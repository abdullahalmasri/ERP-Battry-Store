from models.order import Order


class OrderController:
    def __init__(self):
        self.orders = [
            Order(
                order_id=1,
                battery_id=1011,
                supplier_id=201,
                order_date='2024-01-01',
                delivery_date='2024-05-10',
                status='Delivered'
            ),
            Order(
                order_id=2,
                battery_id=1012,
                supplier_id=202,
                order_date='2024-01-01',
                delivery_date='2024-09-10',
                status='Pending'
            ),
                Order(
                    order_id=3,
                    battery_id=1013,
                    supplier_id=201,
                    order_date='2024-06-01',
                    delivery_date='2024-08-10',
                    status='Shipped'
                ),
        ]

    def place_order(self, order):
        new_order_id = len(self.orders) + 1
        new_order = Order(
            order_id=new_order_id,
            battery_id=int(order['battery_id']),
            supplier_id=int(order['supplier_id']),
            order_date=order['order_date'],
            delivery_date=order['delivery_date'],
            status=order['OrderStatus']
        )
        self.orders.append(new_order)

    def update_order_status(self, order_id, status):
        order = self.find_order_by_id(order_id)
        if order:
            order.update_order_status(status)

    def find_order_by_id(self, order_id):
        for order in self.orders:
            if order.order_id == int(order_id):
                return order
        return None
