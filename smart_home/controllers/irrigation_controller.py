from smart_home.controllers.controller import Controller


class IrrigationController(Controller):
    name = 'IrrigationController'

    def __init__(self, desired_moisture: float = 40):
        super().__init__()
        self.desired_moisture = desired_moisture

    def control_irrigation(self):
        for sensor in self.sensors:
            print(sensor.name, " value: ", sensor.get_value())
            if sensor.get_value() < self.desired_moisture:
                for device in self.devices:
                    if not device.get_state():
                        device.turn_on()
                    sensor.update(device)
            elif sensor.get_value() >= self.desired_moisture:
                for device in self.devices:
                    if device.get_state():
                        device.turn_off()
                    sensor.update(device)

    def update(self):
        print("IrrigationController update")
        self.control_irrigation()