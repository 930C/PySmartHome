from abc import ABC, abstractmethod


class WeatherStationInterface(ABC):

        @abstractmethod
        def get_temperature(self):
            pass

        @abstractmethod
        def get_humidity(self):
            pass

        @abstractmethod
        def get_pressure(self):
            pass