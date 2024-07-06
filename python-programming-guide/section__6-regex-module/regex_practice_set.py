"""
Quenstion Set
---------------------------------------------------------------------------------------------------
1. How would you write a regex to match any valid email address?

2. Construct a regex pattern to validate a phone number format like (123) 456-7890 or 123-456-7890.

3. Create a regex to find all occurrences of the word "color" in a text, including its British spelling "colour".

4. Write a regex to match a valid web URL, including http and https protocols.

6. How can you use regex to match dates in the format YYYY-MM-DD?

7. Formulate a regex to match a string that starts with a capital letter and ends with a period.

8. Develop a regex to extract all hashtags (e.g., #example) from a block of text.

9. Write a regex to match a 16-digit credit card number that may be separated by spaces or dashes every four digits.

10. How would you write a regex to remove all HTML tags from a string?

11. Create a regex to match a username that starts with a letter and can contain letters, numbers, hyphens, and underscores, but must be between 3 and 16 characters long.
---------------------------------------------------------------------------------------------------

"""

import re


class RegexPracticeSet:
    """
    A class containing methods to resolved common regex problem and their solutions
    """

    def __init__(self, input_data):
        self.input_data = input_data

    def find_valid_email(self):
        """
        Extract and prints the valid email address from a given multiline strings

        Args:
         input_data(str): single line or multiline string

        return: valid email address(es)
        """
        email_pattern = r"[0-9a-zA-Z\_\-\.]+[@][a-z\.]+"

        valid_emails = re.findall(email_pattern, self.input_data)
        print(f"Type object of find all: {type(valid_emails)}") #Type object of find all: <class 'list'>
        print(f"Emails Identified: {valid_emails}") # Prints list of valid email addresses


    def find_valid_phone_numbers(self):
        
        phone_number_pattern = r'[0-9\(\)-]+'
        valid_phone_numbers = re.findall(phone_number_pattern, self.input_data)
        print(f"Valid Phone Numbers: {valid_phone_numbers}")


if __name__ == "__main__":

    statement = "Please contact us at support@example.com for assistance."
    statement = "Send your feedback to feedback@example.co.uk or call us."
    statement = "Feel free to get in touch with our support team at support-team@subdomain.example.com 24/7."

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
    regexPracticeSet = RegexPracticeSet(paragraph)
    regexPracticeSet.find_valid_email()
    regexPracticeSet.find_valid_phone_numbers()
