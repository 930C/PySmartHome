import devices
from abc import ABC, abstractmethod


class DeviceFactory(ABC):
    @abstractmethod
    def create_device(self, device_data):
        pass


class LightFactory(DeviceFactory):
    def create_device(self, device_data):
        return devices.Light(device_data["name"])


class ThermostatFactory(DeviceFactory):
    def create_device(self, device_data):
        return devices.Thermostat(device_data["name"], device_data["temperature"])


class SecuritySystemFactory(DeviceFactory):
    def create_device(self, device_data):
        return devices.SecuritySystem(device_data["name"])


class MusicPlayerFactory(DeviceFactory):
    def create_device(self, device_data):
        return devices.MusicPlayer(device_data["name"])


class Controller:
    FACTORY_MAP = {
        "Light": LightFactory(),
        "Thermostat": ThermostatFactory(),
        "SecuritySystem": SecuritySystemFactory(),
        "MusicPlayer": MusicPlayerFactory(),
    }

    def __init__(self, config_data):
        self.device_status = config_data["initial_device_status"]
        self.devices = []
        for device_data in config_data["devices"]:
            factory = self.FACTORY_MAP.get(device_data["type"])
            if factory is not None:
                self.devices.append(factory.create_device(device_data))
            else:
                print(f'Unrecognized device type: {device_data["type"]}')

    def perform_action(self, device, action, *args, **kwargs):
        if hasattr(device, action):
            method = getattr(device, action)
            if callable(method):
                method(*args, **kwargs)
            else:
                raise ValueError(f"{action} is not a method of {device}")
        else:
            raise ValueError(f"{device} does not have a method named {action}")

