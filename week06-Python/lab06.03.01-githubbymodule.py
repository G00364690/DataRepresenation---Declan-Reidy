from github import Github
import requests

# remove the minus sign from the key
g = Github("189b5abe81000b91963056c6eb9f54fac10afd6-5")

repo = g.get_repo("G00364690/Datarepresentation")
print(repo)

# Question 4
print(repo.clone_url)

# Question 5
fileInfo = repo.get_contents("Project.txt")
urlOfFile = fileInfo.download_url

print(urlOfFile)