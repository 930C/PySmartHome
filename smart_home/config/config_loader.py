import yaml
from smart_home.controllers.controller import Controller
from smart_home.controllers.fertilization_controller import FertilizationController
from smart_home.controllers.climate_controller import ClimateController
from smart_home.controllers.humidity_controller import HumidityController
from smart_home.controllers.irrigation_controller import IrrigationController
from smart_home.controllers.lighting_controller import LightingController
from smart_home.devices.climate.fan import Fan
from smart_home.devices.climate.heater import Heater
from smart_home.devices.humidity.humidifier import Humidifier
from smart_home.devices.climate.roller_blind import RollerBlind
from smart_home.devices.fertilization.fertilizer import Fertilizer
from smart_home.devices.irrigation.irrigation_system import IrrigationSystem
from smart_home.devices.irrigation.rainwater_harvesting_system import RainwaterHarvestingSystem
from smart_home.devices.lights.led_light import LEDLight
from smart_home.logging.logger import setup_logger
from smart_home.sensors.fertilization_sensor import FertilizationSensor
from smart_home.sensors.humidity_sensor import HumiditySensor
from smart_home.sensors.temperature_sensor import TemperatureSensor
from smart_home.sensors.irrigation_sensor import IrrigationSensor


# Open-Closed Principle (OCP) -> einfaches Hinzufügen von devices und sensors

class DeviceFactory:
    logger = setup_logger(__name__)

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
        'temperature_sensor': TemperatureSensor,
        'fertilization_sensor': FertilizationSensor,
        "humidity_sensor": HumiditySensor,
        "irrigation_sensor": IrrigationSensor,
    }

    sensor_controller_classes = {
        TemperatureSensor: ClimateController,
        FertilizationSensor: FertilizationController,
        HumiditySensor: HumidityController,
        IrrigationSensor: IrrigationController,
    }

    controller_classes = {
        Fan: ClimateController,
        LEDLight: LightingController,
        Heater: ClimateController,
        Humidifier: HumidityController,
        RollerBlind: ClimateController,
        Fertilizer: FertilizationController,
        IrrigationSystem: IrrigationController,
        RainwaterHarvestingSystem: IrrigationController,
    }

    # TODO: Alarme hinzufügen

    # In dieser Methode wird die Klasse des Geräts für das jeweilige Gerät ermittelt.
    @classmethod
    def create_device(cls, device_info):
        DeviceFactory.logger.info(f'Creating device {device_info["name"]}')
        yaml_device_type = device_info.get('type')
        # Hier wird die Klasse des Geräts für das jeweilige Gerät ermittelt.
        device_class = cls.device_classes.get(yaml_device_type)

        if device_class is not None:
            return device_class(device_info['name'])

        raise ValueError(f'Invalid device type: {yaml_device_type}')

    @classmethod
    def create_sensor(cls, sensor_info):
        DeviceFactory.logger.info(f'Creating sensor {sensor_info["name"]}')
        yaml_sensor_type = sensor_info.get('type')
        sensor_class = cls.sensor_classes.get(yaml_sensor_type)

        if sensor_class is not None:
            return sensor_class(sensor_info['name'])

        raise ValueError(f'Invalid device type: {yaml_sensor_type}')

    # In dieser Methode wird die Klasse des Controllers für das jeweilige Gerät ermittelt.
    @classmethod
    def create_controller(cls, device):
        DeviceFactory.logger.info(f'Creating controller for {device.name}')
        # Hier wird die Klasse des Controllers für das jeweilige Gerät ermittelt.
        controller_class = cls.controller_classes.get(type(device), Controller)
        # Hier wird eine Instanz des Controllers für das jeweilige Gerät erstellt.
        return controller_class(device)


# Single Responsibility Principle (SRP) -> alle Konfigurationsdaten aus einer config file
class ConfigLoader:
    logger = setup_logger(__name__)

    @staticmethod
    def load_config(config_file: str):
        ConfigLoader.logger.info(f'Loading config from {config_file}')
        with open(config_file, 'r') as f:
            config_data = yaml.safe_load(f)
        return config_data
