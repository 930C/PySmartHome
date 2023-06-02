from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton


class MainGui(QMainWindow):
    def __init__(self, smart_home):
        super().__init__()

        self.smart_home = smart_home
        self.setWindowTitle("PySmartHome")

        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        layout = QVBoxLayout()
        self.main_widget.setLayout(layout)

        # Create a button for each device
        for controller in self.smart_home.get_controllers():
            device_button = QPushButton(controller.device.name)
            device_button.clicked.connect(lambda checked, c=controller: c.toggle_device())
            layout.addWidget(device_button)

    def update_ui(self):
        # This function is called whenever the status of a device changes
        for i in range(self.main_widget.layout().count()):
            button = self.main_widget.layout().itemAt(i).widget()
            controller = self.smart_home.get_controller_by_device_id(button.text())
            if controller is not None:
                device = controller.device
                # Update the button text to show the device status
                button.setText(f"{device.name}: {'On' if device.state else 'Off'}")
