from smart_home.controllers.controller import Controller


class HumidityController(Controller):
    name = 'HumidityController'

    def __init__(self, desired_moisture: float = 60):
        super().__init__()
        self.desired_moisture = desired_moisture

    def control_humidity(self):
        for sensor in self.sensors:
            print(sensor.name, " value: ", sensor.get_value())
            if sensor.get_value() < self.desired_moisture:
                for device in self.devices:
                    device.humidify()
                    sensor.update(device)
            elif sensor.get_value() > self.desired_moisture:
                for device in self.devices:
                    device.dehumidify()
                    sensor.update(device)
            else:
                for device in self.devices:
                    if device.get_state():
                        device.turn_off()
                    sensor.update(device)

    def update(self):
        print("HumidityController update")
        self.control_humidity()
