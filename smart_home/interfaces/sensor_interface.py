from abc import ABC, abstractmethod


class SensorInterface(ABC):

    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def set_value(self, value):
        pass
