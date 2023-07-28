from smart_home.controllers.controller import Controller
from smart_home.interfaces.humidity_control_interface import HumidityControlInterface


class HumidityController(Controller):
    name = 'HumidityController'

    def __init__(self, desired_moisture: float = 60):
        super().__init__()
        self.desired_moisture = desired_moisture
        self.logger.info(f'Created controller {self.name} with desired moisture {self.desired_moisture}')

    def control_humidity(self):
        self.logger.info(f'Controlling humidity with desired moisture {self.desired_moisture}')
        sensor_value = self.getStrategy().calculate_value(self.sensors)

        for device in self.devices:
            if sensor_value < self.desired_moisture:
                if isinstance(device, HumidityControlInterface):
                    device.humidify()
            elif sensor_value > self.desired_moisture:
                if isinstance(device, HumidityControlInterface):
                    device.dehumidify()
            else:
                if device.get_state():
                    device.turn_off()
                    
            for sensor in self.sensors:
                sensor.update(device)

    def update(self):
        self.logger.info(f'Updating {self.name}..')
        self.control_humidity()
