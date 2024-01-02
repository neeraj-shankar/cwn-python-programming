import re

phone_text = """
(748) 328-771
(435) 601-342
null
(272) 339-6340
(633) 404-3452
not a number
(761) 870-4420
(890) 166-3349
+44 7070456320
"""

phone_numbers = [
    '(748) 328-771',
    '(435) 601-342',
    'null',
    '(272) 339-6340',
    '(633) 404-3452',
    'not a number',
    '(761) 870-4420',
    '(890) 166-3349',
    '+44 7070456320',
]


"""
shows only those numbers that are inside circle brackets with 3 digits eg- (123)
"""
print("==================================================================================")
print("The matching results using match(): ")
for number in phone_numbers:
    if re.match('\(\d{3}\)', number):
        print(number)

"""
prints the starting index and ending index of searched expression
"""
print("==================================================================================")
print("The matching results using search(): ")
res = re.search('\(761\) 870-4420', phone_text)
span = res.span()
print(span)
print("==================================================================================")

"""
Replace Certain characters from a string using #str.replace()
"""
print("The phone numbers without brackets: ")
alt_phon_text = phone_text.replace('(', '').replace(') ', '').replace('-', '')
print(alt_phon_text)
print("==================================================================================")

"""
Replace the using the # re.sub()
"""
print("The brackets, comma and space removed using sub()")
sub_phone_text = re.sub(r'[^\d\n]', '', phone_text)
print(sub_phone_text)


