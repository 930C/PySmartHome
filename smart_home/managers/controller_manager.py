from typing import List
from smart_home.controllers.controller import Controller
from smart_home.logging.logger import LoggerFactory


# Single Responsibility: This class is responsible for managing all controllers
class ControllerManager:
    def __init__(self, controller_types: dict):
        self.logger = LoggerFactory.setup_logger(ControllerManager.__name__)    # ControllerManager needs a name
        self.controllers = controller_types
        self.logger.info(f'Created controller manager with controllers: {self.controllers}')

    def add_controller(self, controller: Controller):
        self.controllers[controller.name] = controller
        self.logger.info(f'Added controller {controller.name} to controller manager')

    def get_controller(self, name: str) -> Controller:
        self.logger.info(f'Getting controller {name} from controller manager')
        return self.controllers[name]

    def get_controllers(self) -> List[Controller]:
        self.logger.info(f'Getting controllers from controller manager')
        return list(self.controllers.values())
