class Order:
    def __init__(self, order_id, battery_id, supplier_id, order_date, delivery_date, status):
        self.order_id = order_id
        self.battery_id = battery_id
        self.supplier_id = supplier_id
        self.order_date = order_date
        self.delivery_date = delivery_date
        self.status = status

    def place_order(self):
        pass

    def update_order_status(self, status):
        self.status = status

    def track_delivery(self):
        pass
