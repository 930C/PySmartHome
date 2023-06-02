from .device import Device


class Thermostat(Device):
    def __init__(self, device_id, name, temperature=20.5):
        super().__init__(device_id, name)
        self.temperature = temperature
