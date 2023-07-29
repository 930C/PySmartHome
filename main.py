from smart_home.controllers.smart_home_controller import SmartHomeController
from smart_home.logging.logger import LoggerFactory


def main():
    logger = LoggerFactory.setup_logger(__name__)
    logger.info('Staring application..')
    smart_home = SmartHomeController('resources/config.yaml')
    smart_home.start()


if __name__ == "__main__":
    main()
