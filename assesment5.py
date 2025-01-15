#Task: API Interaction Using Requests Library
#Objective:
#Create a Python application that demonstrates the use of GET and POST methods using the requests library. The application will interact with a mock REST API to fetch and send data.
#Scenario:
#You are building a simple application to interact with an online mock API that manages a list of users. The API allows you to:
#Fetch the list of users using a GET request.
#Add a new user using a POST request.
#You will use the following free mock API for this task:
#Base URL: https://jsonplaceholder.typicode.com
#Task Requirements:
#Feature 1: Fetch User Data
#Use a GET request to fetch all users from the endpoint:/users.
#Print the name and email of each user.
#Feature 2: Add a New User
#Use a POST request to add a new user to the API.
#Endpoint: /users.
#Send the following data as JSON in the request:
#json
#Copy code
#{
 #   "name": "John Doe",
  #  "username": "johndoe",
   # "email": "johndoe@example.com"
#}
#Print the response from the API to confirm the user was added.
#Error Handling:
#Handle cases where the API returns an error (e.g., check for status codes).

import requests

# Base URL for the mock API
url = "https://jsonplaceholder.typicode.com"

# Function to fetch user data using GET request
def fetch_users():
    try:
        # Endpoint to fetch users
        response = requests.get(f"{url}/users")
        # Check if the request was successful
        response.raise_for_status()
        
        # Parse the JSON response
        users = response.json()
        
        print("User List:")
        for user in users:
            print(f"Name: {user['name']}, Email: {user['email']}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error: Network issue or invalid request: {req_err}")

# Function to add a new user using POST request
def add_user():
    # Data to be sent as JSON in the POST request
    user_data = {
        "name": "John Doe",
        "username": "johndoe",
        "email": "johndoe@example.com"
    }
    try:
        # Endpoint to add a new user
        response = requests.post(f"{url}/users", json=user_data)
        # Check if the request was successful
        response.raise_for_status()
        
        # Print the response from the API
        print("Response from API after adding the user:")
        print(response.json())
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error: Network issue or invalid request: {req_err}")

# Main function to demonstrate both features
def main():
    print("Fetching user data...")
    fetch_users()
    print("\nAdding a new user...")
    add_user()

if __name__ == "__main__":
    main()
