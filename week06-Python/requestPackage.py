import requests
import json
from xlwt import *

#url = 'https://www.gmit.ie'

#response = requests.get(url)

#print(response.status_code)
#print(response.headers)

# Question 1 a
url = "http://127.0.0.1:5000/cars"
#data = {'reg' : '123','make':'blah','model':'blah-blah','price':1234}

response = requests.get(url) #, json=data)
print(response.status_code)
data = (response.json())

# Question 1 b
for car in data["cars"]:
    print (car)

# Question 1 c
filename = "cars.json"
if filename:
    #write json data
    with open(filename, 'w') as fn:
        json.dump(data, fn, indent=4)

# Question 1 d 

w = Workbook()
ws = w.add_sheet("cars")
#start at row 0, populate header
row = 0;
ws.write(row,0,"reg")
ws.write(row,1,"make")
ws.write(row,2,"model")
ws.write(row,3,"price")
row = row + 1
#loop through car and populate given row
for car in data["cars"]: 
    ws.write(row,0,car["reg"])
    ws.write(row,1,car["make"])
    ws.write(row,2,car["model"])
    ws.write(row,3,car["price"])
    row = row + 1
w.save("cars.xls")




#its the same for put/delete/update etc 
#just change "requests.XYZ" to put/delete/update

