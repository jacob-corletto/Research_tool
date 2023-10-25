from webscraper import *

url = 'https://business.glendora-chamber.org/list/ql/shopping-specialty-retail-23'

url2 = 'https://business.glendora-chamber.org/list/ql/home-garden-12'

url3 = 'https://business.glendora-chamber.org/list/ql/business-professional-services-5'

url4 = 'https://business.glendora-chamber.org/list/ql/restaurants-food-beverages-22'

listings = 'gz-list-card-wrapper col-sm-6 col-md-4'

addresses = 'list-group-item gz-card-address'

numbers = 'list-group-item gz-card-phone'
#list-group-item gz-card-phone

names = 'card-header'

with pd.ExcelWriter('Glendora Contact List.xlsx', engine='xlsxwriter') as writer:
    webscraper(url,listings,names,addresses,numbers).to_excel(writer, sheet_name='shopping-specialty-retail', index=False)
    webscraper(url2,listings,names,addresses,numbers).to_excel(writer, sheet_name='home-garden', index=False)
    webscraper(url3,listings,names,addresses,numbers).to_excel(writer, sheet_name='business-professional-services', index=False)
    webscraper(url4,listings,names,addresses,numbers).to_excel(writer, sheet_name='restaurants-food-beverages', index=False)