import MySQLdb

def connection(db_name):
	db = MySQLdb.connect(	host="localhost", 
							user="root",
							passwd= "vbhv3301",
							db = db_name)

	cur = db.cursor()

	return cur, db

cur, db = connection('musicdb')
name = "HEllo"
link = "safagfgdasgdsagsdgasgsaasdgs"
q = 'insert into songs(name, url, hits) values("%s", "%s", "%d")' % (name, link, 1)
cur.execute(q)
db.commit()