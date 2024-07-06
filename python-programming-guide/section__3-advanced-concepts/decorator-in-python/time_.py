import re

timestamp_pattern = r'(\d{2}):(\d{2}):(\d{2}) (\d{2}-\d{2}-\d{4})'

def reformat_timestamp(timestamp):
    match = re.search(timestamp_pattern, timestamp)
    if match:
        hours, minutes, seconds, date = match.groups()
        reformatted_timestamp = f"{hours}:{minutes} {date}"
        return reformatted_timestamp
    else:
        return None

# Example usage:
text_with_timestamp = "Some sentence here. 10:28:10 10-10-2023"
match = re.search(timestamp_pattern, text_with_timestamp)

if match:
    original_timestamp = match.group(0)
    reformatted_timestamp = reformat_timestamp(original_timestamp)

    if reformatted_timestamp:
        print(f"Original Timestamp: {original_timestamp}")
        print(f"Reformatted Timestamp: {reformatted_timestamp}")
    else:
        print("Invalid timestamp format.")
else:
    print("No timestamp found.")
