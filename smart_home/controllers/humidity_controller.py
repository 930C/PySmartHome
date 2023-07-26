from smart_home.controllers.controller import Controller


class HumidityController(Controller):
    name = 'HumidityController'

    def __init__(self, desired_moisture: float = 60):
        super().__init__()
        self.desired_moisture = desired_moisture
        self.logger.info(f'Created controller {self.name} with desired moisture {self.desired_moisture}')

    def control_humidity(self):
        self.logger.info(f'Controlling humidity with desired moisture {self.desired_moisture}')
        sensor_value = self.getStrategy().calculate_value(self.sensors)

        if sensor_value < self.desired_moisture:
            for device in self.devices:
                device.humidify()
                for sensor in self.sensors:
                 sensor.update(device)
        elif sensor_value > self.desired_moisture:
            for device in self.devices:
                device.dehumidify()
                for sensor in self.sensors:
                    sensor.update(device)
        else:
            for device in self.devices:
                if device.get_state():
                    device.turn_off()
                for sensor in self.sensors:
                    sensor.update(device)

    def update(self):
        self.logger.info(f'Updating {self.name}..')
        self.control_humidity()
