"""
Table of content
-----------------------------------------------------------------------
1. Making Request by passing parameters
2. Response Content
3. Custom Headers
-----------------------------------------------------------------------
"""

import requests


class RequestBasics:

    @staticmethod
    def request_with_params(payload):
        """
        request_with_params sends a get to request along with data in
        URL's query string.

        Args:
          -payload: A quuery string to be passed in the request URL

        Returns: None but prints newly construted URL
        """
        URL = "https://httpbin.org/get"
        r = requests.get(URL, params=payload)
        print(f"Constructed URL with Params: {r.url}")
        # https://httpbin.org/get?first_key=first_value&second_key=value2&second_key=value3

    @staticmethod
    def response_content(url):
        """
        response_content explores accessing response data in text,
        bytes and json format.

        Args:
          -url: API url where request is to be sent

        Returns: None
        """

        r = requests.get(url=url)

        print(f"Response is Automatically Encoded in: {r.encoding}")
        print(f"Response Type: {type(r.text)}\n\nResponse in Bytes: {r.text}")
        # Response Type: <class 'str'>

        # We can specify our own encoding as below
        r.encoding = "ISO-8859-1"
        print(f"User Specified Encoding: {r.encoding}\n")

        # Accessing response in binary (response as bytes)
        print(f"Response Type: {type(r.content)}\n\nResponse in Bytes: {r.content}")
        # Response Type: <class 'bytes'

        # Accessing response in binary (response as bytes)
        print(f"Response Type: {type(r.json())}\n\nResponse in JSON: {r.json()}")
        # Response Type: <class 'dict'>

    @staticmethod
    def custom_headers(url):
        """
        custom_headers sends get requested to a given URL with some
        additional custom headers. Display all response header received
        from the server.

        Args:
          -url: API url where request is to be sent

        Returns: None
        """

        browser_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0"
        headers = {"User-Agent": browser_agent}
        # Sending request without custom headers
        r = requests.get(url, headers=headers)

        # Displaying list of all headers in response
        for header in r.headers.items():
            print(header)


if __name__ == "__main__":

    # URLS for testing use
    req_single_user = "https://reqres.in/api/users/2"

    # query dictionary to be send in URL
    query_dict = {"first_key": "first_value", "second_key": ["value2", "value3"]}
    # RequestBasics.request_with_params(query_dict)

    # Response Content
    RequestBasics.response_content(req_single_user)

    # Test custom headers
    RequestBasics.custom_headers(req_single_user)
