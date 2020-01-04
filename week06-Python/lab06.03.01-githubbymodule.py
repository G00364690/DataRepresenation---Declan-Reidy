from github import Github
import requests

# remove the minus sign from the key
g = Github("32ac307d2ce1061fd8beecb4324002df97b5753-3")

repo = g.get_repo("G00364690/Datarepresentation")
print(repo)

# Question 4
print(repo.clone_url)

# Question 5
fileInfo = repo.get_contents("clone-FDA-Project.txt")
urlOfFile = fileInfo.download_url

print(urlOfFile)