from smart_home.strategies.strategy import Strategy


class Average(Strategy):

    def __init__(self):
        super().__init__("Average")

    def calculate_value(self, data: []) -> float:
        self.logger.info(f'Calculating average value from {len(data)} sensors')
        # iterate over list and return average value
        sum: float = 0
        number_of_sensors: int = len(data)
        for sensor in data:
            sum += sensor.get_value()

        result = sum / number_of_sensors
        self.logger.info(f'Calculated average value: {result}')
        return result
