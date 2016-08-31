"""Script for collecting all the uses urls from fontsinuse.com as of June 28, 2016
"""

import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json

def collect_use_urls():

	uses_urls = []
	start_url_list = ['http://fontsinuse.com/collection/'+str(i) for i in range(1,115)]
	for url in start_url_list:
		print url
		webpage = requests.get(url).text
		soup = BeautifulSoup(webpage, 'lxml')
		for link in soup.findAll("a","gallery-thumb-link"):
			uses_urls += ['fontsinuse.com'+(link.get('href'))]

	with open('uses_urls.json', 'w') as outfile:
		json.dump(uses_urls, outfile) #json array

if __name__ == '__main__':
	collect_use_urls()