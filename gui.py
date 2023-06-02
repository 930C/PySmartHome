from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget


from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QMenu, QMenuBar
from PyQt6.QtGui import QAction

import control
import devices


class MainGui(QMainWindow):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller
        self.setWindowTitle("PySmartHome")

        self.init_ui()

    def init_ui(self):
        menubar = self.menuBar()

        # Jedes Device bekommt ihr eigener Menüpunkt
        for device in self.controller.devices:
            device_menu = menubar.addMenu(device.name)
            print(device.name)

            # Jedes Device bekommt ihre Action
            toggle_action = QAction('Toggle', self)
            toggle_action.triggered.connect(lambda checked, device=device: self.controller.perform_action(device, "toggle"))
            device_menu.addAction(toggle_action)

            # If the device is a Thermostat, add an action to set temperature
            if isinstance(device, devices.Thermostat):
                set_temp_action = QAction('Set Temperature', self)
                set_temp_action.triggered.connect(lambda checked, device=device: self.controller.perform_action(device, "set_temperature", 21))
                device_menu.addAction(set_temp_action)


