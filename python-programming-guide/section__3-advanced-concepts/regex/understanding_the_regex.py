import re
from collections import Counter
"""
Analysing the basic petter in Regex
"""
#######################################################################################################################
# Character classes
#######################################################################################################################

characters_string = "An apple has many health benefits"
matched_character = re.findall(r'[abc]', characters_string)
print(f"The matched list of characters--> {matched_character}")
cleaned_string = re.sub(r'abc', '', characters_string)
print(f"The matched characters using re.sub --> {cleaned_string}")

# finding each extracted character count
character_count = Counter(matched_character)
print(f"The counter of matched characters --> {character_count}")

#######################################################################################################################
# Character class --> [^a-z]
#######################################################################################################################

camel_case = "A camel case word is Usually when first word start with small letter and Second Word Start with Capital"
matching_char = re.findall(r'[^a-z]', camel_case)
print(f"The matched words with pattern [^a-z]--> {matching_char}")
