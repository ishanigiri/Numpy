#ask: JSON Parsing and Handling API Responses
#objctive:
#Create a Python application that demonstrates how to parse JSON data from an API response, handle potential errors, and extract specific information.
#senario:
#You are building a weather information application that fetches current weather data for a city using the OpenWeatherMap API. Your task is to:
#Send a GET request to fetch the weather data.
#Parse the JSON response to extract and display key information.
#Handle errors like invalid API keys, city not found, or network issues.
#Task Requirements:
#Setup:
#Use the open-meteo API:
#Base URL: https://api.open-meteo.com/v1/forecast
#Features:
#Input: Accept a city name from the user.
#Send Request: Use a GET request to fetch weather data for the given city.
#Parse JSON: Extract and display:
#City name
#Temperature (in Celsius)
#Weather description
#Wind speed
#Error Handling:
#Handle errors like:
#Invalid city name (404 error).
#Invalid API key (401 error).
#Network issues

import requests

def get_weather(city_name):
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 0,  # Placeholder for latitude
        "longitude": 0,  # Placeholder for longitude
        "current_weather": "true",
    }

    # Simulating a mapping for city names to coordinates
    city_coordinates = {
        "New York": {"latitude": 40.7128, "longitude": -74.0060},
        "London": {"latitude": 51.5074, "longitude": -0.1278},
        "Tokyo": {"latitude": 35.6895, "longitude": 139.6917},
    }

    if city_name in city_coordinates:
        params["latitude"] = city_coordinates[city_name]["latitude"]
        params["longitude"] = city_coordinates[city_name]["longitude"]
    else:
        print("Error: City not found in the predefined list.")
        return

    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            weather_data = response.json()

            # Extract required information
            temperature = weather_data.get("current_weather", {}).get("temperature")
            wind_speed = weather_data.get("current_weather", {}).get("windspeed")
            weather_description = weather_data.get("current_weather", {}).get("weathercode", "No description available")

            print(f"City: {city_name}")
            print(f"Temperature: {temperature} °C")
            print(f"Weather Description: {weather_description}")
            print(f"Wind Speed: {wind_speed} km/h")
        else:
            print(f"Failed to retrieve data. Status Code: {response.status_code}")
            if response.status_code == 401:
                print("Error: Invalid API key.")
            elif response.status_code == 404:
                print("Error: City not found.")
    except requests.exceptions.RequestException as e:
        print(f"Network error occurred: {e}")

if __name__ == "__main__":
    city = input("Enter the name of the city: ")
    get_weather(city)
