from models.battery import Battery

class BatteryController:
    def __init__(self):
        self.batteries = [
            Battery('12345', 'Active', 100, 'Cool and dry place'),
            Battery('67890', 'Inactive', 50, 'Room temperature'),
            Battery('11223', 'Active', 75, 'Cool and dry place'),
        ]

    def add_battery(self, battery):
        self.batteries.append(battery)

    def update_battery_status(self, battery_id, status):
        battery = self.find_battery_by_id(battery_id)
        if battery:
            battery.update_status(status)

    def find_battery_by_id(self, battery_id):
        for battery in self.batteries:
            if int(battery.battery_id) == battery_id:
                return battery
        return None
