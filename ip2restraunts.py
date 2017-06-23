import requests 
from pprint import pprint


ip = '182.72.248.18'



masala = requests.get('http://ipinfo.io/'+ip+'/loc')
coods = masala.text.rstrip().split(',')
print coods


url = "https://developers.zomato.com/api/v2.1/categories"
header = {"User-agent": "curl/7.47.0", "Accept": "application/json", "user-key": "6baa48b7b901fe406cc45a7c42fee03c"}

url_rest = "https://developers.zomato.com/api/v2.1/search?lat="+coods[0]+"&lon="+coods[1]
response = requests.get(url_rest, headers=header)

pprint(response.json())