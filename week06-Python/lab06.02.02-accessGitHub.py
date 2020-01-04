# question 5 - using my own github key
import requests
import json

apiKey = "32ac307d2ce1061fd8beecb4324002df97b5753-3"
url = "https://api.github.com/repos/G00364690/Datarepresentation"
filename = "repo.json"

response = requests.get(url, auth=("token",apiKey))

repoJSON = response.json()
file = open("repo.json", "w")
json.dump(repoJSON, file, indent=4)