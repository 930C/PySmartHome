class Device:
    def __init__(self, device_id, name):
        self.device_id = device_id
        self.name = name
        self.state = False  # initial state is off

    def toggle(self):
        self.state = not self.state
        print(f"{self.name} is {'on' if self.state else 'off'}")
