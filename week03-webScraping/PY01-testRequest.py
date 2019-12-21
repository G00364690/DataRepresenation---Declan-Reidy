import requests
from bs4 import BeautifulSoup as bs

#question 1
page = requests.get("https://www.football-italia.net/clubs/Inter/news")
print(page)
print("--------")
print(page.content)

#question 2
soup1 = bs(page.content, "html.parser")
print("--------")
print(soup1.prettify()) #verified works


#question 3
with open("../week01-html/Carviewer.html") as fp:
    soup = bs(fp,'html.parser')
    print(soup.prettify())


#question 4
with open("PY03-readOutFile.py", mode="w") as output:
    print(soup.tr, file=output) #verified works 

#question 5
with open("PY03-readOutFile2.py", mode="w") as output:
    rows = soup.findAll("tr")
    for row in rows:
        print("------") #clue from terminal
        print(row, file=output) #verified works 

#question 6
with open("PY03-readOutFile3.py", mode="w") as output:
    rows = soup.findAll("tr")
    for row in rows:
        cols = row.findAll("td")
        for col in cols:
            print("------") #clue from terminal
            print(col.text, file=output) #verified works 

#question 7
with open("PY03-readOutFile4.py", mode="w") as output:
    rows = soup.findAll("tr")
    for row in rows:
        dataList = []
        cols = row.findAll("td")
        for col in cols:
            dataList.append(col.text)
        print(dataList, file=output) #verified works 