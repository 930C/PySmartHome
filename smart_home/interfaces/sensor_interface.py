from abc import ABC, abstractmethod


class SensorInterface(ABC):

    @abstractmethod
    def get_data(self):
        pass