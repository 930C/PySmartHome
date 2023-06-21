from smart_home.managers.controller_manager import ControllerManager


class Zone:
    def __init__(self, name: str, controller_manager: ControllerManager):
        self.name = name
        self.controllerManager = controller_manager
