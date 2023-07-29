from abc import ABC, abstractmethod


class HumidityControlInterface(ABC):

    @abstractmethod
    def humidify(self, level: float):
        pass

    @abstractmethod
    def dehumidify(self, level: float):
        pass
