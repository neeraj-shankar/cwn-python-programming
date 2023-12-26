"""
Python program convert time from 12-hour format (12:00:00 PM) to 24-format ( 12:00:00)
"""

from datetime import datetime


class TimeConversion:
    def __init__(self, in_time):
        self.in_time = in_time

    def convert_to_24_hour_format(self):
        time_obj = datetime.strptime(self.in_time, "%I:%M:%S %p")
        print(f"Parsed Time: {time_obj}--> {time_obj} and Type: {type(time_obj)}")
        # Parsed Time: 1900-01-01 12:00:00--> 1900-01-01 12:00:00 and Type: <class 'datetime.datetime'>

        # convert to 24-hour format
        time_24_hour = time_obj.strftime("%H:%M:%S")
        print(
            f"The time in 24 hour format--> {time_24_hour} and Type: {type(time_24_hour)}"
        )
        # The time in 24 hour format--> 12:00:00 and type: <class 'str'>


if __name__ == "__main__":
    input_time = "12:00:00 PM"
    TimeConversion(input_time).convert_to_24_hour_format()
