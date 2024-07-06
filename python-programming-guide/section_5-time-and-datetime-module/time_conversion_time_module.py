"""
Python program to demonstrate the conversion of time using different ways
"""
import time
from helper_utilities.loggers import logger_setup

logger = logger_setup(__name__)


class TimeConversionModule(object):

    """
    converting the epoch time to 24-hour time format
    """
    @staticmethod
    def epoch_to_24_hour_format():

        # get current_epoch_timestamp using time module
        current_epoch_time = time.time()
        logger.info(f"The current epoch time --> {current_epoch_time}")

        # convert the epoch time into 24-hour time format
        get_localtime_obj = time.localtime(current_epoch_time)
        logger.debug(f"The local time type --> {type(get_localtime_obj)}")
        time_24_hour_format = time.strftime("%H:%M:%S", get_localtime_obj)
        logger.info(f"The current time in 24-hour format is {time_24_hour_format}")


"""
Creating object and calling the methods
"""
TimeConversionModule.epoch_to_24_hour_format()
