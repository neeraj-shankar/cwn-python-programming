Exploring datetime method
-----------------------------------------------------------------------------------------------------------------------

1. datetime.now([tz])
-----------------------------------------------------------
Returns the current local date and time. tz is an optional argument representing the time zone.

2. datetime(year, month, day, hour, minute, second, microsecond, tzinfo)
-----------------------------------------------------------
Returns a datetime object representing a specific date and time.

Formatting and Parsing:
-----------------------------------------------------------
3. strftime(format)
-----------------------------------------------------------
Returns a string representing the datetime object according to the specified format.
Example --> formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

4. strptime(date_string, format)
-----------------------------------------------------------
Parses a string representing a date and time according to the specified format
Example --> parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

Arithmetic Operations:
-----------------------------------------------------------
+ Operator: Allows you to perform arithmetic operations with datetime objects.
Example --> future_datetime = current_datetime + timedelta(days=7)


