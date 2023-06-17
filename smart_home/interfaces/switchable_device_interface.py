from abc import ABC, abstractmethod


class SwitchableDeviceInterface(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def get_state(self):
        pass
