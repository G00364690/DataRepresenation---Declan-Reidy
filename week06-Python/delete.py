import requests

url = "http://127.0.0.1:5000/cars/123"

response = requests.delete(url)

print(response.status_code)
print(response.text)