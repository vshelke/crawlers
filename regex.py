import requests, bs4, re


page = requests.get("http://mp3-pm.info/song/58313660/lyrics_-_DNCE_-_Cake_By_The_Ocean/")

#page = requests.get("http://mp3-pm.info")

soup = bs4.BeautifulSoup(page.content)
link = soup.find_all('a', href=re.compile('^http.*\.mp3$'))

for i in link:
	print i['href']

#	string - matches string
#	. - anything except newline
#	\d - any digit [0-9]
#	\D - not a digit
#	\s - matches whitespace character i.e \r\n\t\f
#	\S - not whitespace
#	\w - matches any alphanumeric word
#	\W - non-word character
#	^ - matches the start of string (^some)
#	$ - matches the end of string (shit$)

#	Character Class

#	[ ] - selects any one character from the set.
#	[^str] - selects characters other than set.

#	Repetitions

#	{x} - match exactly x number of char or class
#	{x,y} - match in range x to y
