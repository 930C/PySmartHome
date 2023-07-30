from smart_home.strategies.strategy import Strategy


class Average(Strategy):

    def __init__(self):
        super().__init__("Average")

    def calculate_value(self, data: [], sensor_type) -> float | None:
        relevant_sensors = [sensor for sensor in data if isinstance(sensor, sensor_type)]
        if len(relevant_sensors) == 0:
            return None

        self.logger.info(f'Calculating average value from {len(relevant_sensors)} sensors')
        # iterate over list and return average value
        sum: float = 0
        number_of_sensors: int = len(relevant_sensors)
        for sensor in relevant_sensors:
            sum += sensor.get_value()

        result = sum / number_of_sensors
        self.logger.info(f'Calculated average value: {result}')
        return result

    def calculate_value_of_all_data(self, data: []) -> float:
        self.logger.info(f'Calculating average value from {len(data)} sensors')
        # iterate over list and return average value
        sum: float = 0
        number_of_sensors: int = len(data)
        for sensor in data:
            sum += sensor.get_value()

        result = sum / number_of_sensors
        self.logger.info(f'Calculated average value: {result}')
        return result
