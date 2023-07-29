from smart_home.controllers.controller import Controller
from smart_home.sensors.irrigation_sensor import IrrigationSensor


class IrrigationController(Controller):
    name = 'IrrigationController'

    def __init__(self, desired_moisture: float = 40):
        super().__init__()
        self.desired_moisture = desired_moisture
        self.logger.info(f'Created controller {self.name} with desired moisture {self.desired_moisture}')

    def control_irrigation(self):
        self.logger.info(f'Controlling irrigation with desired moisture {self.desired_moisture}')
        if len(self.sensors) is not 0:
            sensor_value = self.getStrategy().calculate_value(self.sensors, IrrigationSensor)

            for device in self.devices:
                if sensor_value < self.desired_moisture:
                    if not device.get_state():
                        device.turn_on()
                elif sensor_value >= self.desired_moisture:
                    if device.get_state():
                        device.turn_off()
                for sensor in self.sensors:
                    sensor.update(device)

    def update(self):
        self.logger.info(f'Updating {self.name}..')
        self.control_irrigation()
