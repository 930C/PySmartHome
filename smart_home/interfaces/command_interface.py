from abc import ABC, abstractmethod

from smart_home.managers.controller_manager import ControllerManager


class CommandInterface(ABC):
    @abstractmethod
    def execute(self, controllerManager: ControllerManager):
        pass
