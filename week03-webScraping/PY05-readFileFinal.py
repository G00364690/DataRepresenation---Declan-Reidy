# question 9
from bs4 import BeautifulSoup as bs
import csv

with open("../week01-html/Carviewer.html") as fp:
    soup = bs(fp,'html.parser')

employee_file = open("employee_file2.csv", mode="w")
employee_writer = csv.writer(employee_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)

rows = soup.findAll("tr")
for row in rows:
        
    cols = row.findAll("td")
    dataList = []
    
# question 10       
    for col in cols[0:4]: #limit cols to first 4 (0 up to but not including 4) and eliminate index [4] update and [5] delete
        dataList.append(col.text)
    employee_writer.writerow(dataList) #verified works
employee_file.close()