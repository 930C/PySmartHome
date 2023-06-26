from smart_home.devices.switchable_device import SwitchableDevice


class IrrigationSystem(SwitchableDevice):
    def __init__(self, name: str):
        super().__init__(name)
        self.logger.info(f'Irrigation system {name} created')
