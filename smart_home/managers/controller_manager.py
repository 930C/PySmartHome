from typing import List
from smart_home.controllers.controller import Controller
from smart_home.logging.logger import LoggerFactory
from smart_home.sensors.sensor import Sensor


# Single Responsibility: This class is responsible for managing all controllers
class ControllerManager:
    def __init__(self, controller_types: dict):
        self.logger = LoggerFactory.setup_logger(ControllerManager.__name__)    # ControllerManager needs a name
        self.controllers = controller_types
        self.logger.info(f'Created controller manager with controllers: {self.controllers}')

    def add_controller(self, controller: Controller):
        self.controllers[controller.name] = controller
        self.logger.info(f'Added controller {controller.name} to controller manager')

    def get_controller(self, controller_type: str) -> Controller:
        return self.controllers.get(controller_type)

    def get_controller_by_class(self, controller_type: Controller) -> Controller:
        return self.controllers.get(controller_type)

    def get_controllers(self) -> List[Controller]:
        return list(self.controllers.values())

    def get_sensors(self) -> List[Sensor]:
        sensors = []
        for controller in self.controllers.values():
            sensors += controller.get_sensors()
        return sensors
