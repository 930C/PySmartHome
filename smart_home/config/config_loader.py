from abc import ABC

import yaml

from smart_home import smart_home, rooms
from smart_home.controllers.fertilization_controller import FertilizationController
from smart_home.controllers.climate_controller import ClimateController
from smart_home.controllers.irrigation_controller import IrrigationController
from smart_home.devices.climate.fan import Fan
from smart_home.devices.climate.heater import Heater
from smart_home.devices.climate.humidifier import Humidifier
from smart_home.devices.climate.roller_blind import RollerBlind
from smart_home.devices.fertilization.fertilizer import Fertilizer
from smart_home.devices.irrigation.irrigation_system import IrrigationSystem
from smart_home.devices.irrigation.rainwater_harvesting_system import RainwaterHarvestingSystem
from smart_home.devices.switchable_device import SwitchableDevice
from smart_home.devices.lights.led_light import LEDLight
from smart_home.managers.controller_manager import ControllerManager
from smart_home.rooms.room import Room
from smart_home.rooms.zone import Zone

from smart_home.sensors.sensor import Sensor
from smart_home.sensors.temperature_sensor import TemperatureSensor
# from smart_home.devices.sensors.motion_sensor import MotionSensor

from smart_home.controllers.device_controller import DeviceController
from smart_home.controllers.light_controller import LightController
from smart_home.smart_home import SmartHome


#Open-Closed Principle (OCP) -> einfaches Hinzufügen von devices
class DeviceFactory:
    device_classes = {
        'led_light': LEDLight,
        'fan': Fan,
        'heater': Heater,
        'humidifier': Humidifier,
        'roller_blind': RollerBlind,
        'fertilizer': Fertilizer,
        'irrigation_system': IrrigationSystem,
        'rainwater_harvesting_system': RainwaterHarvestingSystem
    }

    controller_classes = {
        Fan: ClimateController,
        LEDLight: LightController,
        Heater: ClimateController,
        Humidifier: ClimateController,
        RollerBlind: ClimateController,
        Fertilizer: FertilizationController,
        TemperatureSensor: DeviceController,
        IrrigationSystem: IrrigationController,
        RainwaterHarvestingSystem: IrrigationController,
    }

    # TODO: Alarme hinzufügen

    # In dieser Methode wird die Klasse des Geräts für das jeweilige Gerät ermittelt.
    @classmethod
    def create_device(cls, device_info):
        yaml_device_type = device_info.get('type')
        # Hier wird die Klasse des Geräts für das jeweilige Gerät ermittelt.
        device_class = cls.device_classes.get(yaml_device_type)

        if device_class is not None:
            return device_class(device_info['id'], device_info['name'])

        raise ValueError(f'Invalid device type: {yaml_device_type}')

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


# Single Responsibility Principle (SRP) -> alle Konfigurationsdaten aus einer config file
class ConfigLoader:

    @staticmethod
    def load_config(self, config_file: str):
        with open(self.config_file, 'r') as f:
            config_data = yaml.safe_load(f)
        return config_data

