import re

timestamp_pattern = r'\d{2}:\d{2}:\d{2} \d{2}-\d{2}-\d{4}'

# Example usage:
text_with_timestamp = "Some 10:28:10 10-10-2023 sentence here."
match = re.search(timestamp_pattern, text_with_timestamp)

if match:
    timestamp = match.group(0)
    print(f"Timestamp found: {timestamp}")
else:
    print("No timestamp found.")
