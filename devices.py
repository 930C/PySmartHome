class Device:
    def __init__(self, name):
        self.name = name

    def toggle(self):
        raise NotImplementedError


class Light(Device):
    def __init__(self, name):
        super().__init__(name)
        self.status = False

    def toggle(self):
        self.status = not self.status
        print(f"{self.name} Light status: {'On' if self.status else 'Off'}")


class Thermostat(Device):
    def __init__(self, name, temperature):
        super().__init__(name)
        self.temperature = temperature

    def toggle(self):
        print(f"{self.name} does not support toggle operation")

    def set_temperature(self, temperature):
        self.temperature = temperature
        print(f"{self.name} Temperature set to: {self.temperature}")


class SecuritySystem(Device):
    def __init__(self, name):
        super().__init__(name)
        self.status = False

    def toggle(self):
        self.status = not self.status
        print(f"{self.name} Security System status: {'Activated' if self.status else 'Deactivated'}")


class MusicPlayer(Device):
    def __init__(self, name):
        super().__init__(name)
        self.status = False

    def toggle(self):
        self.status = not self.status
        print(f"{self.name} Music Player status: {'Playing' if self.status else 'Paused'}")
