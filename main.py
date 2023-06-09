from smart_home.controllers.smart_home_controller import SmartHomeController
from smart_home.logging.logger import LoggerFactory


def main():
    # Single Responsibility Principle (SRP) -> alle Konfigurationsdaten aus einer config file
    # smart_home = load_config('resources/config.yaml')

    # app = QApplication(sys.argv)
    #
    # gui = MainGui(smart_home)
    # gui.show()

    # sys.exit(app.exec())

    logger = LoggerFactory.setup_logger(__name__)
    logger.info('Staring application..')
    smart_home = SmartHomeController('resources/config.yaml')
    smart_home.update()


if __name__ == "__main__":
    main()

# TODO: Erstelle ein Zustandsmanagement für die Geräte
