import re 


paragraph = """
    Contact us at support@example.com or call (123) 456-7890 for support.
    Our UK branch can be reached at uk-office@example.co.uk or at +44 20 7946 0958.
    Please avoid using emails like user@@example.com or phone numbers formatted as 123-45-6789.
    You can also visit our website at https://www.example.com for more information.
    For job applications, email your resume to careers@example.com or fax it to 1-800-555-1234.
    Beware of phishing URLs like http://www.example.fakewebsite or emails from noreply@example..com.
    Our developer's blog can be found at http://devblog.example.org - lots of great articles!
    Feel free to reach out to our sales team at sales-team@subdomain.example.com or at 555.123.4567.
    Invalid URLs such as www.example@.com or phone numbers like (123) 456-789 are not correct.
    For partnerships, contact us at partners@example.com or visit our LinkedIn page at https://www.linkedin.com/company/example-inc.

    """

# caret(^): Matches the
print(re.findall("^World", "Hello World!"))  # Output: ['Hello']
caret_match = re.findall("^Contact", paragraph)
print(f"Match retured using caret: {caret_match}")

# asterisk(*)
matched_occurences = re.findall("pho*", paragraph)
print(f"Matched occurence: {matched_occurences}")