from smart_home.devices.adjustable_device import AdjustableDevice


class Fertilizer(AdjustableDevice):
    def __init__(self, name: str):
        super().__init__(name)

    def fertilize(self, amount: float):
        self.set_level(amount)
        if not self.state:
            self.turn_on()
        self.fertilizing()

    def stop_fertilizing(self):
        self.turn_off()

    def fertilize_once(self, amount: float):
        self.set_level(amount)
        self.turn_on()
        self.fertilizing()
        self.turn_off()

    def fertilizing(self):
        print("Fertilizing ", self.name, " with ", self.value, " amount")

