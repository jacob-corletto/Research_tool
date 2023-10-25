import requests
import pandas as pd
import csv
from bs4 import BeautifulSoup

# Define the URL of the specific category page

def webscraper(url,listings,names,addresses,numbers):
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
    # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the business listings in the category
        business_listings = soup.find_all('div', class_ =listings)

        data1 = []

        for listing in business_listings:
            # Extract the address
            try:
                address = listing.find('li',class_ = addresses).text.replace("\n","")
            except:
                address = ''

            # Extract the phone number
            try:
                phone_number = listing.find('li',class_=numbers).text.replace("\n","")
            except:
                phone_number = ''

            #extract name
            try:
                name = listing.find('div',class_=names).text.replace("\n","")
            except:
                name = ''

            #extract link
            try:
                link = listing.find('a').get('href')
            except:
                link = ''

            # Print the information
            new_entry = {
            'Name': f'{name}',
            "Address": f'{address}',
            "Phone Number": f'{phone_number}',
            "Link": f'{link}',
            "Contacted":'',
            "Notes":''
            }
            data1.append(new_entry)
            print(data1)

            df1 = pd.DataFrame(data1)
        return df1
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return data1




