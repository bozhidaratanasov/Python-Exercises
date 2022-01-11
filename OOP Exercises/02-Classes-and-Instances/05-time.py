from datetime import datetime
class Time:
    max_hours = 23
    max_minutes = 59
    max_second = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        time_str = f"{str(self.hours)}::{str(self.minutes)}::{str(self.seconds)}"
        return datetime.strptime(time_str, '%H::%M::%S').time()

    def next_second(self):
        self.seconds += 1
        if self.seconds > self.max_second:
            self.minutes += 1
            self.seconds = 0
        if self.minutes > self.max_minutes:
            self.hours += 1
            self.minutes = 0
        if self.hours > self.max_hours:
            self.hours = 0

        return self.get_time()