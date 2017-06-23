import os, requests, bs4, pymongo, re, urlparse, MySQLdb

#		TODO
#	*manage relative links
#	*Invalid link problem
#	*Encoding problem
#	*Show status
#	*Check flow
#	*Add name of song to db
#	*Implement indexing
#	*Minimize db checking and lookup

#		GLOBAL 

seed = "http://mp3-pm.info/"
crawldb = "musicdb"
search_pattern = "^http.*\.mp3$"

#		FUNCTIONS	

def db_connect(host, port):
	client = pymongo.MongoClient(host, port)
	db = client[crawldb]
	return db

def get_soup(link):
	try:
		page = requests.get(link)
		soup = bs4.BeautifulSoup(page.content,"html.parser")
		return soup
	except:
		pass

def pattern(regix, soup):
	pool = soup.find_all('a', { 'href' : regix})
	return pool

def add_link_traveldb(t_pool):
	global db
	for a in t_pool:
		link = a['href']
		#Managing relative links***
		if link.startswith('/'):
			link = seed + link

		if db.travel.find_one({"url": link}) == None and link.startswith("http"):
			ins =	db.travel.insert_one({
				"url": link,
				"isVisited": False
				})

def add_link_maindb(m_pool):
	global db
	for a in m_pool:
		link = a['href']
		#Manage relative links
		if db.main.find_one({"url": link}) == None:
			name = link.split('/')[-1][:-4]
			ins =	db.main.insert_one({
				"name": name,
				"url": link,
				"timesPlayed": 0
				})

def connection():
	Mydb = MySQLdb.connect(	host="localhost", 
							user="root",
							passwd= "vbhv3301",
							db = "musicdb")

	cur = Mydb.cursor()

	return cur, Mydb

def load_mysqldb(m_pool):
	global Mdb, cur
	for a in m_pool:
		link = a['href']
		name = link.split('/')[-1][:-4]
		q = 'insert into songs(name, url, hits) values("%s", "%s", "%d")' % (name, link, 1)
		cur.execute(q)
		Mdb.commit()

def get_next_link():
	global db
	v = db.travel.find_one({"isVisited": False})
	if v == None:
		return None
	a = db.travel.update_one({"url": v['url']},
		{"$set": {"isVisited": True}})
	return	v['url']

def crawl(current):
	soup = get_soup(current)
	travel_pool = pattern(re.compile(".*") , soup)
	if travel_pool:
		add_link_traveldb(travel_pool)
	main_pool = pattern(re.compile(search_pattern), soup)
	if main_pool:
		add_link_maindb(main_pool)
		load_mysqldb(main_pool)
		print "loaded into both databases"

#		FLOW

db = db_connect('localhost', 27017)
cur, Mdb = connection()
print "Database Connected!"
crawl(seed)
while True:
	crawl(get_next_link())
