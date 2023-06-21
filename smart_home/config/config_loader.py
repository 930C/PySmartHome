import yaml
from smart_home.controllers.controller import Controller
from smart_home.controllers.fertilization_controller import FertilizationController
from smart_home.controllers.climate_controller import ClimateController
from smart_home.controllers.irrigation_controller import IrrigationController
from smart_home.controllers.lighting_controller import LightingController
from smart_home.devices.climate.fan import Fan
from smart_home.devices.climate.heater import Heater
from smart_home.devices.climate.humidifier import Humidifier
from smart_home.devices.climate.roller_blind import RollerBlind
from smart_home.devices.fertilization.fertilizer import Fertilizer
from smart_home.devices.irrigation.irrigation_system import IrrigationSystem
from smart_home.devices.irrigation.rainwater_harvesting_system import RainwaterHarvestingSystem
from smart_home.devices.lights.led_light import LEDLight
from smart_home.sensors.temperature_sensor import TemperatureSensor


# Open-Closed Principle (OCP) -> einfaches Hinzufügen von devices
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

    sensor_classes = {
        'temperature_sensor': TemperatureSensor
    }

    sensor_controller_classes = {
        TemperatureSensor: ClimateController
    }

    controller_classes = {
        Fan: ClimateController,
        LEDLight: LightingController,
        Heater: ClimateController,
        Humidifier: ClimateController,
        RollerBlind: ClimateController,
        Fertilizer: FertilizationController,
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
            return device_class(device_info['name'])

        raise ValueError(f'Invalid device type: {yaml_device_type}')

    @classmethod
    def create_sensor(cls, sensor_info):
        yaml_sensor_type = sensor_info.get('type')
        sensor_class = cls.sensor_classes.get(yaml_sensor_type)

        if sensor_class is not None:
            return sensor_class(sensor_info['name'])

        raise ValueError(f'Invalid device type: {yaml_sensor_type}')

    # In dieser Methode wird die Klasse des Controllers für das jeweilige Gerät ermittelt.
    @classmethod
    def create_controller(cls, device):
        # Hier wird die Klasse des Controllers für das jeweilige Gerät ermittelt.
        controller_class = cls.controller_classes.get(type(device), Controller)
        # Hier wird eine Instanz des Controllers für das jeweilige Gerät erstellt.
        return controller_class(device)


# Single Responsibility Principle (SRP) -> alle Konfigurationsdaten aus einer config file
class ConfigLoader:

    @staticmethod
    def load_config(config_file: str):
        with open(config_file, 'r') as f:
            config_data = yaml.safe_load(f)
        return config_data
