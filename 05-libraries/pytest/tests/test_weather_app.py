
from samples.weather_app import get_weather_adivce

import pytest_mock

def test_get_weather_advice(mocker):

    mock_get = mocker.patch('weather.requests.get')

    # 2. Configure the mock to return a specific "fake" response
    mock_get.return_value.json.return_value = {"weather": "Rainy"}

    result = get_weather_adivce()

    # 4. ASSERT
    assert result == "Bring an umbrella!"
    # Verify the API was actually called once
    mock_get.assert_called_once_with("https://api.weather.com/v1/status")


