
# Single Search
#https://www.nobroker.in/property/rent/bangalore/
# Marathahalli?
# searchParam=W3sibGF0IjoxMi45NTY5MjQsImxvbiI6NzcuNzAxMTI3LCJwbGFjZUlkIjoiQ2hJSlZ3a2RWYlFUcmpzUkdVa2VmdGVVZUZrIiwicGxhY2VOYW1lIjoiTWFyYXRoYWhhbGxpIn1d
# &radius=2.0&sharedAccomodation=0&type=BHK3&city=bangalore&locality=Marathahalli

#https://www.nobroker.in/property/rent/bangalore/multiple?searchParam=W3sibGF0IjoxMi45NTY5MjQsImxvbiI6NzcuNzAxMTI3LCJwbGFjZUlkIjoiQ2hJSlZ3a2RWYlFUcmpzUkdVa2VmdGVVZUZrIiwicGxhY2VOYW1lIjoiTWFyYXRoYWhhbGxpIn0seyJsYXQiOjEyLjkzMDQyNzgsImxvbiI6NzcuNjc4NDA0LCJwbGFjZUlkIjoiQ2hJSkwtazBMblVUcmpzUnJtcVliNlkwc3NJIiwicGxhY2VOYW1lIjoiQmVsbGFuZHVyIn0seyJsYXQiOjEyLjkzODg3ODcsImxvbiI6NzcuNzQxMjA0NywicGxhY2VJZCI6IkNoSUoyUndKNFljTnJqc1JINWhVY0dPOG5fayIsInBsYWNlTmFtZSI6IlZhcnRodXIifV0=
# &radius=2.0&sharedAccomodation=0&type=BHK3,BHK2&city=bangalore&locality=Marathahalli,&locality=Bellandur,&locality=Varthur

#Multiple Search
#https://www.nobroker.in/property/rent/bangalore/
# multiple?
# searchParam=W3sibGF0IjoxMi45NTY5MjQsImxvbiI6NzcuNzAxMTI3LCJwbGFjZUlkIjoiQ2hJSlZ3a2RWYlFUcmpzUkdVa2VmdGVVZUZrIiwicGxhY2VOYW1lIjoiTWFyYXRoYWhhbGxpIn0seyJsYXQiOjEyLjkzMDQyNzgsImxvbiI6NzcuNjc4NDA0LCJwbGFjZUlkIjoiQ2hJSkwtazBMblVUcmpzUnJtcVliNlkwc3NJIiwicGxhY2VOYW1lIjoiQmVsbGFuZHVyIn0seyJsYXQiOjEyLjkzODg3ODcsImxvbiI6NzcuNzQxMjA0NywicGxhY2VJZCI6IkNoSUoyUndKNFljTnJqc1JINWhVY0dPOG5fayIsInBsYWNlTmFtZSI6IlZhcnRodXIifV0=
# &radius=2.0&sharedAccomodation=0&type=BHK3,BHK2&city=bangalore&locality=Marathahalli,&locality=Bellandur,&locality=Varthur

# https://www.nobroker.in/property/2-bhk-apartment-for-rent-in-marathahalli-bangalore-for-rs-14000/ff80818159877fa6015987cbab260aed/detail


from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import itertools
import time
import random


sample_link = "https://www.nobroker.in/property/rent/bangalore/multiple?searchParam=W3sibGF0IjoxMi45NTY5MjQsImxvbiI6NzcuNzAxMTI3LCJwbGFjZUlkIjoiQ2hJSlZ3a2RWYlFUcmpzUkdVa2VmdGVVZUZrIiwicGxhY2VOYW1lIjoiTWFyYXRoYWhhbGxpIn0seyJsYXQiOjEyLjkzMDQyNzgsImxvbiI6NzcuNjc4NDA0LCJwbGFjZUlkIjoiQ2hJSkwtazBMblVUcmpzUnJtcVliNlkwc3NJIiwicGxhY2VOYW1lIjoiQmVsbGFuZHVyIn0seyJsYXQiOjEyLjkzODg3ODcsImxvbiI6NzcuNzQxMjA0NywicGxhY2VJZCI6IkNoSUoyUndKNFljTnJqc1JINWhVY0dPOG5fayIsInBsYWNlTmFtZSI6IlZhcnRodXIifV0=&radius=2.0&sharedAccomodation=0&type=BHK3,BHK2&city=bangalore&locality=Marathahalli,&locality=Bellandur,&locality=Varthur"
header =  {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie':'deviceType=web; headerFalse=false; isMobile=false',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62',
    }
headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
base_url = "https://www.nobroker.in/property/rent/bangalore/multiple?searchParam=W3sibGF0IjoxMi45NTY5MjQsImxvbiI6NzcuNzAxMTI3LCJwbGFjZUlkIjoiQ2hJSlZ3a2RWYlFUcmpzUkdVa2VmdGVVZUZrIiwicGxhY2VOYW1lIjoiTWFyYXRoYWhhbGxpIn0seyJsYXQiOjEyLjkzMDQyNzgsImxvbiI6NzcuNjc4NDA0LCJwbGFjZUlkIjoiQ2hJSkwtazBMblVUcmpzUnJtcVliNlkwc3NJIiwicGxhY2VOYW1lIjoiQmVsbGFuZHVyIn0seyJsYXQiOjEyLjkzODg3ODcsImxvbiI6NzcuNzQxMjA0NywicGxhY2VJZCI6IkNoSUoyUndKNFljTnJqc1JINWhVY0dPOG5fayIsInBsYWNlTmFtZSI6IlZhcnRodXIifV0="
radius = "5.0"
room_type = "BHK3,BHK2"
locality = "locality=Marathahalli,&locality=Bellandur,&locality=Varthur"

exclude_list = ["standalone", "independent"]

response = get(sample_link,headers=header)

# dataframe
titles = []
addresses = []
rents = []
sizes = []
deposits = []

# for testing if scraping of website is allowed...
print(response)
# print(response.text[:1000])
# Parsing through html page
html_soup = BeautifulSoup(response.text,'html.parser')
house_containers = html_soup.find_all('div', class_="infinite-scroll-component")
# house_containers = html_soup.findAll('article', attrs={'role': 'article'})

# if(house_containers != []):

print(f"Number of Properties : {len(house_containers)}")

print(type(house_containers))

matches = html_soup.select('article')

#print(f"Matches : {matches}")

print(f"Type {type(matches)} & Length : {len(matches)}")

    
    # properties = house_containers.find_all('article')
    
    # print(f"Properies #{properties}")
    
for container in matches:
    
    title = (container.find('h2','heading-6').find('span').text.replace('\n',''))
    
    if any(exclude in title.lower() for exclude in exclude_list):
        print(f"Skipping : {title}")
    
    else:
        try:
            #rent = int(container.find("div", {"id": "minimumRent"}).text.replace(',',''))
            rent = (container.find("div", {"id": "minimumRent"}).text.replace(',',''))
            rents.append(rent)
        except:
            rents.append("-")
        try:
            # size = int(container.find_all('h3')[0].find_all('span')[0].text.replace(',',''))
            # size = int(container.find("div", {"id": "unitcode"}).text.replace(',',''))
            #size = int(container.find("div", {"id": "unitcode"}).text.replace(',',''))
            size = (container.find("div", {"id": "unitCode"}).text.replace(',',''))
            sizes.append(size)
        except:
            sizes.append("-")
        try:
            deposit = (container.find("div", {"id": "roomType"}).text.replace(',',''))
            deposits.append(deposit)
        except:
            deposits.append("-")
        
        address = (container.find('div','overflow-ellipsis').text.replace('\n',''))
        # deposit = int(container.select('div#roomType').text.replace(',',''))
        # deposit = (container.find("div", {"id": "roomType"}).text.replace(',',''))
        # size = (container.find("div", {"id": "unitCode"}).text.replace(',',''))
        # rent = (container.find("div", {"id": "minimumRent"}).text.replace(',',''))
        
        print(f"Name : {title} & Address : {address} & {size}sqft & Deposit : {deposit}/- & Rent : {rent}/- ")
        
        titles.append(title)
        addresses.append(address)

# creating dataframe to save data in .csv format
cols = ['Title', 'Address', 'Rent(Rs)', 'Deposit(Rs)', 'Size(Acres)',]

blr = pd.DataFrame({'Title': titles,
                        'Address': addresses,
                        'Rent(Rs)': rents,
                        'Deposit(Rs)': deposits,
                        'Size(Acres)': sizes,})[cols]
blr.to_csv('blr_rent.csv')