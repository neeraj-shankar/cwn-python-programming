"""
------------------------------------------------------------------------------
Problem Statement: Converting time from 12-hour format (12:00:00 PM) to 
24-format ( 12:00:00)
------------------------------------------------------------------------------
"""

from datetime import datetime


class TimeConversion:
    """
    A class for converting time from 12-hour format to 24-hour format.

    Attributes:
        in_time (str): The input time string in 12-hour format.
    """

    def __init__(self, in_time):
        self.in_time = in_time

    def convert_to_24_hour_format(self):
        """
        Convert the input time string to 24-hour format and print the result.

        Raises:
            ValueError: If the input time string format is invalid.

        Example:
            >>> TimeConversion("3:00:00 PM").convert_to_24_hour_format()
            Parsed Date Time: 1900-01-01 15:00:00 --> 15:00:00 and Type: <class 'datetime.datetime'>
            The time in 24-hour format: 15:00:00 and Type: <class 'str'>
        """

        time_obj = datetime.strptime(self.in_time, "%I:%M:%S %p")
        print(f"Parsed Date Time: {time_obj}--> {time_obj} and Type: {type(time_obj)}")
        # Parsed Time: 1900-01-01 12:00:00--> 1900-01-01 12:00:00 and Type: <class 'datetime.datetime'>

        # convert to 24-hour format
        time_24_hour = time_obj.strftime("%H:%M:%S")
        print(
            f"The time in 24 hour format--> {time_24_hour} and Type: {type(time_24_hour)}"
        )
        # The time in 24 hour format--> 12:00:00 and type: <class 'str'>


if __name__ == "__main__":
    input_time = "3:00:00 PM"
    TimeConversion(input_time).convert_to_24_hour_format()
