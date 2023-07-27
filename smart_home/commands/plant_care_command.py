from smart_home.controllers.fertilization_controller import FertilizationController
from smart_home.controllers.humidity_controller import HumidityController
from smart_home.controllers.irrigation_controller import IrrigationController
from smart_home.controllers.lighting_controller import LightingController
from smart_home.devices.fertilization.fertilizer import Fertilizer
from smart_home.devices.humidity.humidifier import Humidifier
from smart_home.devices.irrigation.irrigation_system import IrrigationSystem
from smart_home.devices.lights.led_light import LEDLight
from smart_home.interfaces.command_interface import CommandInterface
from smart_home.logging.logger import LoggerFactory
from smart_home.managers.controller_manager import ControllerManager


class PlantCareCommand(CommandInterface):
    error_Codes_to_device_types: dict = {
        "000": None,
        "999": None,
        "001": IrrigationSystem,
        "002": IrrigationSystem,
        "010": Fertilizer,
        "020": Humidifier,
        "021": Humidifier,
        "030": LEDLight,
        "031": LEDLight,
    }

    error_Codes_to_need_Device: dict = {
        "000": None,
        "999": None,
        "001": True,
        "002": False,
        "010": True,
        "020": True,
        "021": False,
        "030": True,
        "031": False,
    }

    error_Codes_to_controller_type = {
        "000": None,
        "999": None,
        "001": IrrigationController,
        "002": IrrigationController,
        "010": FertilizationController,
        "020": HumidityController,
        "021": HumidityController,
        "030": LightingController,
        "031": LightingController,
    }

    def __init__(self, error_code: str):
        self.error_code = error_code
        self.device_type = self.error_Codes_to_device_types.get(error_code)
        self.needs_device = self.error_Codes_to_need_Device.get(error_code)
        self.controller_type = self.error_Codes_to_controller_type.get(error_code)
        self.logger = LoggerFactory.setup_logger('PlantCareCommand')
        self.logger.info(
            f'Created PlantCareCommand with error code {error_code}. Affected device type: {self.device_type}. Zone needs device: {self.needs_device}. Controller type: {self.controller_type}')

    def execute(self, controllerManager: ControllerManager):
        self.logger.info(f'Executing PlantCareCommand with error code {self.error_code}')
        if self.controller_type or self.device_type or self.needs_device is None:
            return
        controller = controllerManager.get_controller(self.controller_type)
        if controller is None:
            return
        for device in controller.devices:
            if self.needs_device:
                device.get(self.device_type).turn_on()
            else:
                device.get(self.device_type).turn_off()
