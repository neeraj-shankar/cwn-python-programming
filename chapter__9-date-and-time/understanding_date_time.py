"""
A python program to undertsand the use case of date and time module
"""
import datetime
from datetime import timedelta
class UnderstandingDateTimeModule:

    """
    Expores the base terms and constants used in this module
    """
    @staticmethod
    def basic_terms():

        # Print the minimum year
        min_year = datetime.MINYEAR
        max_year = datetime.MAXYEAR
        print(f"The miniumum year that can be entered is -- {min_year}, while the maximum can be --> {max_year}")
        print("===================================================================================================")

        # exploring different classes in datetime module
        idate = datetime.date
        itime = datetime.time
        idatetime = datetime.datetime
        itime_delta = datetime.timedelta
        itime_zone = datetime.tzinfo

        print(f"The date class --> {idate} and the time class --> {itime}")
        print(f"The datetime class is --> {idatetime} and time delta  classis --> {itime_delta}")

        print(f"The current zone info class --> {itime_zone}")
        print("===================================================================================================")
        

    
    @staticmethod
    def explore_time_delta():

        delta = timedelta(
                    days=50,
                    seconds=27,
                    microseconds=10,
                    milliseconds=29000,
                    minutes=5,
                    hours=8,
                    weeks=2
                )           
        print(delta)


"""
Calling the different functions
"""

UnderstandingDateTimeModule.basic_terms()
UnderstandingDateTimeModule.explore_time_delta()