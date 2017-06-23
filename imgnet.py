import requests as rq
from subprocess import call

url = "http://image-net.org/api/text/imagenet.synset.geturls?wnid=n04409515"
dir = "pos/"

rep = rq.get(url)

lst = rep.content.split("\n")

for i in lst:
	call(["wget", i])
