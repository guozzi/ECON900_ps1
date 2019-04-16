import urllib.request
import os
import time
import datetime
from time import sleep
from random import randint

if not os.path.exists("html_files"):
	os.mkdir("html_files")

pages = [str(i) for i in range(1,1066)]
start_time = time.time()
requests = 0

for page in pages:
    f = open("html_files/bggPage" + page + ".html", "wb")
    response = urllib.request.urlopen('https://boardgamegeek.com/browse/boardgame/page/' + page)
    html = response.read()
    f.write(html)
    f.close()
    sleep(randint(5,20))
    requests += 1  #request status monitor
    elapsed_time = time.time() - start_time
    print('Request:{}; Frequency: {} requests/min'.format(requests, requests/elapsed_time * 60))
