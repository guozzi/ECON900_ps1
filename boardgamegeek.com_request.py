import urllib.request
import os
import time
import datetime

if not os.path.exists("html_files"):
	os.mkdir("html_files")

pages = [str(i) for i in range(1,5)]


for page in pages:
    f = open("html_files/bggPage" + page + ".html", "wb")
    response = urllib.request.urlopen('https://boardgamegeek.com/browse/boardgame/page/' + page)
    html = response.read()
    f.write(html)
    f.close()

