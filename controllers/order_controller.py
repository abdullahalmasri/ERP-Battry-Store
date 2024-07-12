from models.order import Order

class OrderController:
    def __init__(self):
        self.orders = []

    def place_order(self, order):
        self.orders.append(order)

    def update_order_status(self, order_id, status):
        order = self.find_order_by_id(order_id)
        if order:
            order.update_order_status(status)

    def find_order_by_id(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None
