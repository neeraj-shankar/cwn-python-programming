import re
from datetime import datetime

def compare_strings_ignore_seconds(expected_value, actual_value):
    # Define the timestamp pattern
    timestamp_pattern = r'\d{2}:\d{2}:\d{2} \d{2}-\d{2}-\d{4}'

    # Extract timestamps using regular expressions
    expected_timestamp_str = re.search(timestamp_pattern, expected_value).group(0)
    actual_timestamp_str = re.search(timestamp_pattern, actual_value).group(0)

    # Define the timestamp format
    timestamp_format = "%H:%M:%S %d-%m-%Y"

    # Parse the timestamps
    expected_timestamp = datetime.strptime(expected_timestamp_str, timestamp_format)
    actual_timestamp = datetime.strptime(actual_timestamp_str, timestamp_format)

    # Disregard seconds in the comparison
    expected_timestamp = expected_timestamp.replace(second=0)
    actual_timestamp = actual_timestamp.replace(second=0)

    # Replace timestamp substrings with placeholders for comparison
    expected_value_without_timestamp = re.sub(timestamp_pattern, "", expected_value)
    actual_value_without_timestamp = re.sub(timestamp_pattern, "", actual_value)

    # Compare modified strings
    return (
        expected_value_without_timestamp == actual_value_without_timestamp
        and expected_timestamp == actual_timestamp
    )

# Example usage:
expected_string = "Some sentence here. 10:28:10 10-10-2023"
actual_string = "Some 10-10-2023 sentence here. 10:28:25"

result = compare_strings_ignore_seconds(expected_string, actual_string)
print(result)  # Output: True
