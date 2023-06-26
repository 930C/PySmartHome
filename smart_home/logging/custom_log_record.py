import logging


class CustomLogRecord(logging.LogRecord):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.levelname = f"{self.levelname:<5}"
        self.module = f"{self.module:<24}"
