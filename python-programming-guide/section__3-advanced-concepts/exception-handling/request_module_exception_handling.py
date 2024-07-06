"""
A Python program to handle exceptions that can occur during Https requests
"""
import requests

class HandleRequestsExceptions:

    """
    A simple get request to google
    """
    def get_google(self):
        correct_url = "https://www.google.com"
        incorrect_url = "https://www.google.com/not-found/"
        try:
            req = requests.get(url=correct_url)
            req.raise_for_status()
        
        except requests.exceptions.HTTPError as e :

            return (f"The Http Errror occurred --> {e.args[0]}")






""" 
Class Object and function calls
"""
obj = HandleRequestsExceptions()

# Calling the get_google function
get_google_status = obj.get_google()
print(get_google_status)

