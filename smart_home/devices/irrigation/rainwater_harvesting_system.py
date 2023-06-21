# Schalte dies ein, wenn es Regnet
# Schalte dies aus, wenn es nicht Regnet weil der Tank voll ist
# Der Tank ist wegen Mücken und Algen abgedeckt
from smart_home.devices.switchable_device import SwitchableDevice


class RainwaterHarvestingSystem(SwitchableDevice):
    def __init__(self, name: str):
        super().__init__(name)
