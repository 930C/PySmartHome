from smart_home.logging.logger import LoggerFactory
from smart_home.managers.controller_manager import ControllerManager


class Zone:
    def __init__(self, name: str, controller_manager: ControllerManager):
        self.name = name
        self.logger = LoggerFactory.setup_logger(self.name)
        self.controllerManager = controller_manager
        self.logger.info(f'Created zone {self.name} with controller manager {controller_manager}')
