from sample_data import print_message, get_config_value, fetch_data_from_api

def test_capfd_fixture(capfd):

    # Call the function that prints stdout
    print_message()

    # capture the output using capfd
    out, err = capfd.readouterr()
    expected_message = f"This is capfd() method test\n"
    assert out == expected_message
    assert err == ""

def test_get_config_value(monkeypatch):
    # Set environment variable for testing
    monkeypatch.setenv("MY_CONFIG_KEY", "test value")

    # Call the function that reads the environment value
    actual_value = get_config_value("MY_CONFIG_KEY")

    # Assert that the function returns expected value
    assert actual_value == "test value"


def test_fetch_data_from_api(monkeypatch):
    """
    :Overview test_fetch_data_from_api verifies whether fetch_data_from_api
              works fine. That is the api able send request to external API
              and returns the response data in Json Format.
    :param monkeypatch: To Mock External API Calls with mock data and avoid making actual api call
    :return: None
    """
    # Define a mock response data
    mock_response_data = {"key": "value"}

    # Define a mock function to replace requests.get()
    def mock_get(*args, **kwargs):
        class MockResponse:
            def json(self):
                return mock_response_data

        return MockResponse()

    # Monkeypatch requests.get() with the mock function
    monkeypatch.setattr("requests.get", mock_get)

    # Call the function that fetches data from the API
    data = fetch_data_from_api("https://api.example.com/data")

    # Assert that the function returns the expected data
    assert data == mock_response_data
