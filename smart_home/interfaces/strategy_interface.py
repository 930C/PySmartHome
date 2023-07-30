from abc import ABC, abstractmethod


class StrategyInterface(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def calculate_value(self, data: [], sensor_type):
        pass

    @abstractmethod
    def calculate_value_of_all_data(self, data: []):
        pass
