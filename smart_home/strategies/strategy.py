from smart_home.interfaces.strategy_interface import StrategyInterface
from smart_home.logging.logger import LoggerFactory


class Strategy(StrategyInterface):
    def __init__(self, name: str):
        self.name = name
        self.logger = LoggerFactory.setup_logger(self.name)
        self.logger.info(f'Created strategy {self.name}')
