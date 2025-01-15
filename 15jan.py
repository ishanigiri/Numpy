import requests
#github API URL for trending repositories(python as an example)
url = "https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc"
#send GET request to the github API
response = requests.get(url)
if response.status_code == 200:
    print("Trending Repositories fetched successfully!\n")
    data = response.json()
    # Display the top 5 trending repositories
    for repo in data["items"][:5]:
        name = repo["name"]
        owner = repo["owner"]["login"]
        description = repo.get("description", "No description available.")
        stars = repo["stargazers_count"]
        print(f"Repo Name: {name}\nOwner: {owner}\nStars: {stars}\nDescription: {description}\n")
else:
    print(f"Failed to retrieve data. Status Code: {response.status_code}")