import requests
import json
from xlwt import *

url = "https://api.github.com/users/andrewbeattycourseware/followers"

response = requests.get(url)
data = response.json()


filename = "githubusers.json"
with open(filename, "w") as fn:
    json.dump(data, fn, indent=4)

w = Workbook()
ws = w.add_sheet("followers")
#start at row 0, populate header row
row = 0;
ws.write(row,0,"login")
ws.write(row,1,"id")
ws.write(row,2,"node_id")
ws.write(row,3,"avatar_url")
ws.write(row,4,"gravatar_id")
ws.write(row,5,"url")
ws.write(row,6,"html_url")
ws.write(row,7,"followers_url")
ws.write(row,8,"following_url")
ws.write(row,9,"gists_url")
ws.write(row,10,"starred_url")
ws.write(row,11,"subscriptions_url")
ws.write(row,12,"organizations_url")
ws.write(row,13,"repos_url")
ws.write(row,14,"events_url")
ws.write(row,15,"received_events_url")
ws.write(row,16,"type")
ws.write(row,17,"site_admin")
row = row + 1
#loop through car and populate given row
for field in data[0:17]: 
    ws.write(row,0,field["login"])
    ws.write(row,1,field["id"])
    ws.write(row,2,field["node_id"])
    ws.write(row,3,field["avatar_url"])
    ws.write(row,4,field["gravatar_id"])
    ws.write(row,5,field["url"])
    ws.write(row,6,field["html_url"])
    ws.write(row,7,field["followers_url"])
    ws.write(row,8,field["following_url"])
    ws.write(row,9,field["gists_url"])
    ws.write(row,10,field["starred_url"])
    ws.write(row,11,field["subscriptions_url"])
    ws.write(row,12,field["organizations_url"])
    ws.write(row,13,field["repos_url"])
    ws.write(row,14,field["events_url"])
    ws.write(row,15,field["received_events_url"])
    ws.write(row,16,field["type"])
    ws.write(row,17,field["site_admin"])
    row = row + 1
w.save("githubusers.xls")
