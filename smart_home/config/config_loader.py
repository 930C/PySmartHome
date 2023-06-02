import yaml

from smart_home.devices.device import Device
from smart_home.devices.light import Light
from smart_home.devices.thermostat import Thermostat

from smart_home.devices.sensor import Sensor
from smart_home.devices.temperature_sensor import TemperatureSensor
from smart_home.devices.motion_sensor import MotionSensor

from smart_home.controllers.device_controller import DeviceController
from smart_home.controllers.light_controller import LightController
from smart_home.controllers.thermostat_controller import ThermostatController
from smart_home.smart_home import SmartHome


class DeviceFactory:
    device_classes = {
        'device': Device,
        'light': Light,
        'thermostat': Thermostat,
        'sensor': Sensor,
        'temperature_sensor': TemperatureSensor,
        'motion_sensor': MotionSensor
    }

    controller_classes = {
        Device: DeviceController,
        Light: LightController,
        Thermostat: ThermostatController,
        Sensor: DeviceController,
        TemperatureSensor: DeviceController,
        MotionSensor: DeviceController
    }

    # In dieser Methode wird die Klasse des Geräts für das jeweilige Gerät ermittelt.
    @classmethod
    def create_device(cls, device_info):
        device_type = device_info.get('type')
        # Hier wird die Klasse des Geräts für das jeweilige Gerät ermittelt.
        device_class = cls.device_classes.get(device_type)

        if device_class is not None:
            return device_class(device_info['id'], device_info['name'])

        raise ValueError(f'Invalid device type: {device_type}')

    # In dieser Methode wird die Klasse des Controllers für das jeweilige Gerät ermittelt.
    @classmethod
    def create_controller(cls, device):
        # Hier wird die Klasse des Controllers für das jeweilige Gerät ermittelt.
        controller_class = cls.controller_classes.get(type(device), DeviceController)
        # Hier wird eine Instanz des Controllers für das jeweilige Gerät erstellt.
        return controller_class(device)


def load_config(config_file):
    with open(config_file, 'r') as f:
        config_data = yaml.safe_load(f)

    smart_home = SmartHome()

    for device_info in config_data.get('devices', []):
        device = DeviceFactory.create_device(device_info)
        controller = DeviceFactory.create_controller(device)
        smart_home.add_controller(controller)

    return smart_home
