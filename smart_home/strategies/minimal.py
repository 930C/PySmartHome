from smart_home.strategies.strategy import Strategy


class Minimal(Strategy):

    def __init__(self):
        super.__init__(self, "Minimal")

    def calculate_value(self, data: [], sensor_type) -> float:
        relevant_sensors = [sensor for sensor in data if isinstance(sensor, sensor_type)]
        self.logger.info(f'Calculating minimal value from {len(relevant_sensors)} sensors')
        # iterate over list and return minimal value
        min: float = 100
        for sensor in relevant_sensors:
            if sensor.get_value() < min:
                min = sensor.get_value()

        self.logger.info(f'Calculated minimal value: {min}')
        return min

    def calculate_value_of_all_data(self, data: []) -> float:
        self.logger.info(f'Calculating minimal value from {len(data)} sensors')
        # iterate over list and return minimal value
        min: float = 100
        for sensor in data:
            if sensor.get_value() < min:
                min = sensor.get_value()

        self.logger.info(f'Calculated minimal value: {min}')
        return min
