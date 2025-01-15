import requests
#url of the public API
url = "https://jsonplaceholder.typicode.com/posts"
#send a GET request to the API
response = requests.get(url)
#Check if the request was succesful (status code 200)
if response.status_code ==200:
    print("Data fetched successfully!\n")
    #Parse the JSON data
    data = response.json()
    # Display the first 3 posts
    for post in data[:3]:
        print(f"Post ID: {post["id"]}")
        print(f"Title: {post["title"]}")
        print(f"Body: {post["body"]}\n")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")