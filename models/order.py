from datetime import datetime


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

    def update_order_status(self, new_status):
        self.status = new_status

    def track_delivery(self):
        # Define the dates as strings
        order_date_str = self.order_date
        delivery_date_str = self.delivery_date

        # Parse the date strings to datetime objects
        order_date = datetime.strptime(order_date_str, '%Y-%m-%d')
        delivery_date = datetime.strptime(delivery_date_str, '%Y-%m-%d')

        # Calculate the difference between the two dates
        date_difference = delivery_date - order_date

        # Get the current date
        current_date = datetime.now()

        # Calculate the number of days remaining until the delivery date
        days_remaining = (delivery_date - current_date).days
        return days_remaining
