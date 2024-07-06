from datetime import datetime
from datetime import date
from datetime import timedelta
from datetime import time
from datetime import timezone

# current date and time given timezone
current_time_local = datetime.now()
print(f"Current Local Time: {current_time_local} and {type(current_time_local)}") # Current Local Time: 2024-06-12 08:25:48.485404 and <class 'datetime.datetime'>


# Get the current date
today = date.today()
print("Current date:", today) #Current date: 2024-06-12

# Create a specific date
independence_day = date(1947, 8, 15)
print(f"date of india independence: {independence_day}") # date of india independence: 1947-08-15

# calculate the difference between two dates
delta = today - independence_day
print(f"lets celebrate {delta.days} days of independence") # lets celebrate 28061 of independence

# add 7 days to current
one_week_later = today + timedelta(days=7)
print(f"One Week Later date: {one_week_later}")


# create specific time
noon = time(12, 30, 10)
print(f"Noon Time: {noon}") 

# combine date time
lunch_datetime = datetime.combine(today, noon)
print(f"Today's Lunch Date and Time: {lunch_datetime} and {type(lunch_datetime)}") # Today's Lunch Date and Time: 2024-06-12 12:30:10 and <class 'datetime.datetime'>


# Parse a string into a datetime object
date_string = "2024-06-12 12:30:10"  # <class 'str'>

date_time_obj = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(date_time_obj, type(date_time_obj)) # 2024-06-12 12:30:10 <class 'datetime.datetime'>

given_time = "2023-10-10 11:00:00 PM"


# strptime: string parse time - used to create a datetime object from a string representing a date and time and a corresponding format string.
sample_time = datetime.strptime(given_time, r"%Y-%m-%d %I:%M:%S %p")
print(
    f"Resultant Datetime obj: {sample_time} and {type(sample_time)}"
)  # Resultant Datetime obj: 2023-10-10 23:00:00 and <class 'datetime.datetime'>

# Convert the datetime object to a timestamp
timestamp = sample_time.timestamp()
print(f"Timestamp for local time: {timestamp}") # Timestamp for local time: 1696959000.0

# For a UTC datetime object
dt_object_utc = datetime(2023, 10, 10, 12, 10, 30, 10, tzinfo=timezone.utc)
print(f"UTC Date Time: {dt_object_utc}") # UTC Date Time: 2023-10-10 12:10:30.000010+00:00

timestamp_utc = date_time_obj.timestamp()
print(f"Timestamp UTC: {timestamp_utc}") # Timestamp UTC: 1718175610.0
print(f"Timestamp in in integer: {int(timestamp_utc)}")


# string format time- format a datetime object as a string according to a specified format string.
current_datetime = datetime.now()
formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(
    f"String Representation of date time: {formatted_date} and {type(formatted_date)}"
)  # String Representation of date time: 2024-06-12 14:58:34 and <class 'str'>

# 
current_timestamp=int(datetime.now().timestamp())
print(f"Current Timestamp: {current_timestamp}") # Current Timestamp: 1719996807


print(datetime.utcnow())