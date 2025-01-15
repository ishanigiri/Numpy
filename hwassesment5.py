#Homework: Fetch and save weather data from an API.
import requests
import json

# Base URL for the Open-Meteo API
url = "https://api.open-meteo.com/v1/forecast"

# Predefined city coordinates (latitude and longitude)
city_coordinates = {
    "kathmandu": (27.7103, 85.3222),
    "pokhara": (28.2096, 83.9856),
    "janakpur": (26.7271, 85.9407)
}

# Function to fetch weather data using GET request
def fetch_weather(city_name):
    if city_name.lower() not in city_coordinates:
        print(f"Error: City '{city_name}' not found in the predefined list.")
        return None

    # Get latitude and longitude of the city
    lat, lon = city_coordinates[city_name.lower()]
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": "true"
    }

    try:
        # Send GET request to the API
        response = requests.get(url, params=params)
        # Check if the request was successful
        response.raise_for_status()
        
        # Parse the JSON response
        weather_data = response.json()
        
        # Extract relevant data
        current_weather = weather_data.get("current_weather", {})
        weather_details = {
            "city": city_name,
            "temperature": current_weather.get("temperature"),
            "weather_code": current_weather.get("weathercode"),
            "wind_speed": current_weather.get("windspeed")
        }
        return weather_details
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error: {req_err}")
    return None

# Function to save weather data to a file
def save_weather_to_file(weather_data, file_name="weather_data.txt"):
    try:
        # Save data in JSON format for readability
        with open(file_name, "w") as file:
            json.dump(weather_data, file, indent=4)
        print(f"Weather data saved to {file_name}")
    except Exception as e:
        print(f"Error saving weather data: {e}")

# Main function to demonstrate fetching and saving weather data
def main():
    # Get user input for city name
    city_name = input("Enter a city name (Kathmandu, Pokhara, Janakpur): ").strip()

    # Fetch weather data
    print(f"Fetching weather data for {city_name}...")
    weather_data = fetch_weather(city_name)

    if weather_data:
        # Display fetched data
        print("Fetched Weather Data:")
        for key, value in weather_data.items():
            print(f"{key.capitalize()}: {value}")

        # Save data to a file
        save_weather_to_file(weather_data)

if __name__ == "__main__":
    main()
