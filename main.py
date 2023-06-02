import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

import gui
import config
import control

def main():
    # Erstellen die Anwendung
    app = QApplication(sys.argv)

    # Lade Config
    config_data = config.load_config("config.json")

    # Initialisiere Control-Modul
    controller = control.Controller(config_data)

    # erstelle das GUI und gebe controller weiter
    main_gui = gui.MainGui(controller)

    # Zeige das GUI
    main_gui.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
