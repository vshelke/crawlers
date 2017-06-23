#	Amazon Scraper

import requests, bs4

search_link = "http://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords="

query = raw_input("Item: ")
query = '+'.join(query.split())

page = requests.get(search_link + query)
page.raise_for_status()

soup = bs4.BeautifulSoup(page.text)

products = soup.findAll('div' , { 'class' : 's-item-container'})

products[0]['title']

# for i in products:

# 	print i

	# name = i.find('h2' , { 'class' : 'a-size-medium a-color-null s-inline  s-access-title  a-text-normal'}).get_text()
	# cost = i.find('span' , { 'class' : 'a-size-base a-color-price s-price a-text-bold'}).get_text()

 #  	print name + " <--> " + cost


#print products[0]['title']

