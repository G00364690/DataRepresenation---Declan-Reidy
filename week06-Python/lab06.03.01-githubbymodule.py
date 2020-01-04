from github import Github
import requests

# remove the minus sign from the key
g = Github("47d8d1f0600ffbd0e02d03e94269e6c4db029eb2")

repo = g.get_repo("https://github.com/G00364690/DataRepresenation---Declan-Reidy.git")
#print(repo.clone_url)