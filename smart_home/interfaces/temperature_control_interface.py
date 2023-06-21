from abc import ABC, abstractmethod


class TemperatureControlInterface(ABC):

    @abstractmethod
    def cool(self):
        pass

    @abstractmethod
    def heat(self):
        pass
