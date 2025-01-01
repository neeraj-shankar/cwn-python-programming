"""
Session Objects
-----------------------------------------------------------------------
- The Session object allows you to persist certain parameters across requests.
- A Session object has all the methods of the main Requests API.
-----------------------------------------------------------------------
"""
import requests
# Persist some cookies acrros all requests
s = requests.Session()

s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('https://httpbin.org/cookies')

print(r.text)
# '{"cookies": {"sessioncookie": "123456789"}}'