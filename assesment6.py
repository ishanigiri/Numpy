# Task: JSON Parsing and Handling API Responses

# Objective:
# Create a Python application that demonstrates how to parse JSON data from an API response,
# handle potential errors, and extract specific information.

# Scenario:
# You are building a weather information application that fetches current weather data for a city
# using the OpenWeatherMap API. Your task is to:
# 1. Send a GET request to fetch the weather data.
# 2. Parse the JSON response to extract and display key information.
# 3. Handle errors like invalid API keys, city not found, or network issues.

# Task Requirements:

# Setup:
# Use the open-meteo API:
# Base URL: https://api.open-meteo.com/v1/forecast

# Features:
# Input: Accept a city name from the user.
# Send Request: Use a GET request to fetch weather data for the given city.
# Parse JSON: Extract and display:
# - City name
# - Temperature (in Celsius)
# - Weather description
# - Wind speed

# Error Handling:
# Handle errors like:
# - Invalid city name (404 error).
# - Invalid API key (401 error).
# - Network issues.


import requests

def get_weather_data(city_name):
    # Base URL for Open-Meteo API
    base_url = "https://api.open-meteo.com/v1/forecast"
    
    # Parameters for the API request
    params = {
        'latitude': None,  # Will be populated by geolocation data
        'longitude': None,  # Will be populated by geolocation data
        'current_weather': 'true'
    }
    
    # Use a geocoding API or hardcode latitude/longitude for specific cities
    city_coordinates = {
        "kathmandu" : (27.7103, 85.3222),
        "pokhara" : (28.2096, 83.9856),
        "janakpur" : (26.7271, 85.9407)   
    }
    
    # Check if city is in our predefined list
    if city_name not in city_coordinates:
        print(f"City '{city_name}' not found.")
        return
    
    # Get the latitude and longitude from the predefined coordinates
    lat, lon = city_coordinates[city_name]
    params['latitude'] = lat
    params['longitude'] = lon

    try:
        # Send GET request to Open-Meteo API
        response = requests.get(base_url, params=params)
        
        # Raise an exception for invalid responses
        response.raise_for_status()
        
        # Parse the JSON response
        weather_data = response.json()

        # Extracting information from the JSON response
        current_weather = weather_data.get('current_weather', {})
        
        # Output the extracted data
        print(f"Weather in {city_name}:")
        print(f"Temperature: {current_weather.get('temperature')}°C")
        print(f"Weather description: {current_weather.get('weathercode')}")
        print(f"Wind Speed: {current_weather.get('windspeed')} km/h")
        
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 401:
            print("Error: Invalid API Key!")
        elif response.status_code == 404:
            print("Error: City not found!")
        else:
            print(f"HTTP error occurred: {http_err}")
    
    except requests.exceptions.RequestException as req_err:
        print(f"Error: Network issues or invalid request: {req_err}")
    
# User input for city name
city_name = input("Enter a city name: ").strip()
get_weather_data(city_name)