import re

timestamp_pattern = r'(\d{2}):(\d{2}):(\d{2}) (\d{2}-\d{2}-\d{4})'
timestamp_pattern = r'(\d{1}):(\d{2}):(\d{2})'

def reconstruct_time(match):
    hours, minutes, _= match.groups()
    reformatted_timestamp = f"{hours}:{minutes}"
    return reformatted_timestamp


text_with_timestamp = "Some sentence here at 10:28:10 on 10-10-2023. I am not sure"
text_with_timestamp ="VAT Numbers validated at 6:36:01 am on 08 Nov 2023. Full validation details are available in the Document Repository."
modified_text = re.sub(timestamp_pattern, reconstruct_time, text_with_timestamp)

print(f"Original Text: {text_with_timestamp}")
print(f"Modified Text: {modified_text}")
