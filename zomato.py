# import requests as r

# url = "https://developers.zomato.com/api/v2.1/categories"
# headers = {'Accept': 'application/json', "user_key" : "6baa48b7b901fe406cc45a7c42fee03c"}
# #payload = { "user-key" : "6baa48b7b901fe406cc45a7c42fee03c" }
# req = r.get(url, headers=headers)
# print req.text

import requests
from pprint import pprint

url = "https://developers.zomato.com/api/v2.1/categories"
header = {"User-agent": "curl/7.47.0", "Accept": "application/json", "user-key": "6baa48b7b901fe406cc45a7c42fee03c"}


url_rest = "https://developers.zomato.com/api/v2.1/search?lat=13.0833&lon=80.2833"



response = requests.get(url_rest, headers=header)

pprint(response.json())