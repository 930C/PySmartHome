import sys
from PyQt6.QtWidgets import QApplication

from smart_home.config.config_loader import load_config
from smart_home.gui.main_gui import MainGui


def main():
    #Single Responsibility Principle (SRP) -> alle Konfigurationsdaten aus einer config file
    smart_home = load_config('resources/config.yaml')

    app = QApplication(sys.argv)

    gui = MainGui(smart_home)
    gui.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
