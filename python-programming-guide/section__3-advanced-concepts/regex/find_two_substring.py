import re

sentence = "The quick brown fox jumps over the lazy dog."
event_name = "OSPF Adjacency Failed on Device CI9500-Rack3-1.fra-lab.net Interface Tunnel12 with Neighbor 11.11.11.11"
# Use a regular expression to find the words "quick" and "fox"
raw_expression = r"\b(quick|fox)\b"

ospf_interface = r"\b(OSPF Adjacency Failed|Interface)\b"
matches = re.findall(raw_expression, sentence)

string_match = re.findall(ospf_interface, event_name)

# Print the matches
print(matches)
print(f'The matched names - {string_match}')
