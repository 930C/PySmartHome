from smart_home.devices.sensor import Sensor


class TemperatureSensor(Sensor):
    def __init__(self, device_id, name, value=21.5):
        super().__init__(device_id, name, value)
