from datetime import datetime

class DecimalTime(object):
    def __init__(self):
        self.current_time = None
        self.decimal_time = None
        self._interval = 0.432 # seconds
        self._seconds_since_midnight = None
        self._seconds_per_minute = 100
        self._minutes_per_hour = 100
        self._hours_per_day = 20

    def _get_current_time(self):
        self.current_time = datetime.now()
        self._seconds_since_midnight = (self.current_time - self.current_time.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()

    def _convert_time(self):
        decimal_seconds_since_midnight = self._seconds_since_midnight / self._interval
        hour = (decimal_seconds_since_midnight // (self._seconds_per_minute * self._minutes_per_hour)) - 10
        minute =
        time_string = "{} {}".format(date, time)

    def print_time(self):
        self._get_current_time()
        self._convert_time()
        print()

DecimalTime().print_time()
