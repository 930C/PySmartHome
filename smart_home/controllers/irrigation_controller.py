from smart_home.controllers.controller import Controller

class IrrigationController(Controller):
    name = 'IrrigationController'

    def __init__(self, desired_moisture: float = 40):
        super().__init__()
        self.desired_moisture = desired_moisture
        self.logger.info(f'Created controller {self.name} with desired moisture {self.desired_moisture}')

    def control_irrigation(self):
        self.logger.info(f'Controlling irrigation with desired moisture {self.desired_moisture}')
        for sensor in self.sensors:
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
        self.logger.info(f'Updating {self.name}..')
        self.control_irrigation()
