import requests
import csv
from bs4 import BeautifulSoup as bs

#question 11 - navigate to page 2 changing the last digit from 1 to 2
#https://www.myhome.ie/residential/mayo/property-for-sale?page=2

# question 12 - code to read page 2
page = requests.get("https://www.myhome.ie/residential/mayo/property-for-sale?page=2")
soup = bs(page.content, "html.parser") 
#print(soup.prettify())

# question 13 - searched for Westport

# question 14
listings = soup.find("div" , class_="PropertyListingCard") #changed to find from findAll
#print(listings.div.prettify()) #added .div

# question 15
price = listings.find(class_="PropertyListingCard__Price").text
print(price)

# question 16
address = listings.find(class_="PropertyListingCard__Address").text
print(address)

# question 17
listings = soup.findAll("div" , class_="PropertyListingCard")
for listing in listings:
    entryList = []

    price = listing.find(class_="PropertyListingCard__Price").text
    entryList.append(price)
    address = listing.find(class_="PropertyListingCard__Address").text
    entryList.append(address)

    print(entryList)


# question 18
home_file = open("Lab03MyHome.csv", mode="w")
home_writer = csv.writer(home_file, delimiter="\t", quotechar='"', quoting=csv.QUOTE_MINIMAL)

listings = soup.findAll("div" , class_="PropertyListingCard")
for listing in listings:
    entryList = []

    price = listing.find(class_="PropertyListingCard__Price").text
    entryList.append(price)
    address = listing.find(class_="PropertyListingCard__Address").text
    entryList.append(address)

    print(entryList)

    home_writer.writerow(entryList)
home_file.close()