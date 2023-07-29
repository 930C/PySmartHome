from smart_home.controllers.controller import Controller
from smart_home.interfaces.temperature_control_interface import TemperatureControlInterface
from smart_home.interfaces.humidity_control_interface import HumidityControlInterface
from smart_home.sensors.humidity_sensor import HumiditySensor
from smart_home.sensors.temperature_sensor import TemperatureSensor


class ClimateController(Controller):
    name = 'ClimateController'

    def __init__(self, desired_temperature: float = 21,desired_moisture: float = 60):
        super().__init__()
        self.desired_temperature = desired_temperature
        self.logger.info(f'ClimateController {self.name} with {self.desired_temperature} as desired temperature created')
        self.desired_moisture = desired_moisture
        self.logger.info(f'Created controller {self.name} with desired moisture {self.desired_moisture}')

    def control_temperature(self):
        self.logger.info(f'Controlling climate with desired temperature {self.desired_temperature}')
        relevant_sensors = [sensor for sensor in self.sensors if isinstance(sensor, TemperatureSensor)]
        if len(relevant_sensors) is not 0:
            sensor_value = self.getStrategy().calculate_value(self.sensors, TemperatureSensor)

            for device in self.devices:
                if isinstance(device, TemperatureControlInterface):
                    if sensor_value < self.desired_temperature:
                        device.heat()
                    elif sensor_value > self.desired_temperature:
                        device.cool()
                    else:
                        if device.get_state():
                            device.turn_off()

                    for sensor in self.sensors:
                        if isinstance(sensor, TemperatureSensor):
                            sensor.update(device)

    def control_humidity(self):
        self.logger.info(f'Controlling humidity with desired moisture {self.desired_moisture}')
        relevant_sensors = [sensor for sensor in self.sensors if isinstance(sensor, HumiditySensor)]
        if len(relevant_sensors) is not 0:
            sensor_value = self.getStrategy().calculate_value(self.sensors, HumiditySensor)

            for device in self.devices:
                if isinstance(device, HumidityControlInterface):
                    if sensor_value < self.desired_moisture:
                        device.humidify()
                    elif sensor_value > self.desired_moisture:
                        device.dehumidify()
                    else:
                        if device.get_state():
                            device.turn_off()

                    for sensor in self.sensors:
                        if isinstance(sensor, HumiditySensor):
                            sensor.update(device)

    def update(self):
        self.logger.info(f'Updating {self.name}..')
        self.control_temperature()
        self.control_humidity()