from smart_home.strategies.strategy import Strategy


class Maximal(Strategy):

    def __init__(self):
        super.__init__(self, "Maximal")

    def calculate_value(self, data: [], sensor_type) -> float:
        relevant_sensors = [sensor for sensor in data if isinstance(sensor, sensor_type)]
        self.logger.info(f'Calculating maximal value from {len(relevant_sensors)} sensors')
        # iterate over list and return maximal value
        max: float = 0
        for sensor in relevant_sensors:
            if sensor.get_value() > max:
                max = sensor.get_value()

        self.logger.info(f'Calculated maximal value: {max}')
        return max

    def calculate_value_of_all_data(self, data: []) -> float:
        self.logger.info(f'Calculating maximal value from {len(data)} sensors')
        # iterate over list and return maximal value
        max: float = 0
        for sensor in data:
            if sensor.get_value() > max:
                max = sensor.get_value()

        self.logger.info(f'Calculated maximal value: {max}')
        return max

