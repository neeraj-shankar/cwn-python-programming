import requests

# Create a function that gives weather advice
def get_weather_adivce():

    response = requests.get("https://api.weather.com/v1/status")

    data = response.json()

    if data["weather"] =="Rainy":
        return f"Carry an umbrella with you."

    return "Enjoy the sunny day"
