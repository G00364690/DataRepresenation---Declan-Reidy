import requests
import json

dataString = {'reg' : '191 D 54321','make':'Renault','model':'Laguna','price':25000}


url = "http://127.0.0.1:5000/cars"

response = requests.post(url, json=dataString)
print(response.status_code)