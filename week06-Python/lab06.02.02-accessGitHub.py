# question 5 - using my own github key
import requests
import json

apiKey = "189b5abe81000b91963056c6eb9f54fac10afd6-5"
url = "https://api.github.com/repos/G00364690/Datarepresentation"
filename = "repo.json"

response = requests.get(url, auth=("token",apiKey))

repoJSON = response.json()
file = open("repo.json", "w")
json.dump(repoJSON, file, indent=4)