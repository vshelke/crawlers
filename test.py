import requests, hashlib, bs4, re, pymongo

# seed = "http://www.thefreesite.com/"
# page = requests.get(seed)
# soup = bs4.BeautifulSoup(page.content,"html.parser")
# #print page.text
# links = soup.find_all('a', { 'href' : re.compile(".*")})
# for i in links:
# 	if i['href'].startswith("http"):
# 		print "hello"

# test_str = "http://cs1.mp3.pm/download/58313660/UUg3cklCT3UvZUJLVGRaZUxwM1J6UCtLbTkySWdlWWNuRVA3aGtXYWJ1bGQyUnhoam0yTkdqUHlXR3gzbWdSNXVBb2huQTA5a2dmbmpSZ3FVSTE0VGEyZUx1eHowaGh2bml3R21MUU5HY0tNRWFIci9tWkJ5VGkybVFaeTJxNHg/lyrics_-_DNCE_-_Cake_By_The_Ocean_(mp3.pm).mp3"

# print test_str.split('/')[-1].split('.')[0]



client = pymongo.MongoClient('localhost', 27017)
db = client['vaibhav']
res = db.test.insert_one({"url":"sfdaf"})

# ts()
# ins = db.lol.insert_one({"url":"http://randomusik.tk"})

#CREATE INDEX WHEN RUNNING CRAWLER FOR THE FIRST TIME------------------------

# db.nasacollection.ensure_index([
#       ('Content', 'text'),
#       ('Launch_Date', 'text'),
#       ('Phase','text')
#   ],
#   name="nasadb_index",
#   weights={
#       'Phase':2,
#       'Content':10,
#       'Launch_Date':5	
#   }
# )
# CREATE INDEX END ----------------------------------

# for i in links:
# 	if db.urls.find_one({"url": i['href']}) == None:

# 		tmp = db.urls.insert_one({
# 				"url": i['href'],
# 				"text": i.get_text(),
# 				"isVisited": False,
# 				"checked": 0
# 				})
		
# 	else:

	
# 		#print "not new"
# 		pass
# res = db.urls.update_one(
# 	{"url": "http://www.thefreesite.com/"},
# 	{"$set":{"isVisited": True}})

# v = db.urls.find_one({"isVisited": False})
# print v['url']

# 	DUMPS

# pool = soup.find_all('a', href=re.compile(seed))
# rem = db.urls.drop()
# t =  db.urls.find()
# $for l in t:
	
# 	print l['url']


# print seed.split('.')[1]

# obj = hashlib.md5(seed.encode())
# print obj.hexdigest()
