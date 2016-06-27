"""Script for scraping information from fontsinuse.com as of June 24, 2016
"""

import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json






def parse_font_page(html_str, id):
	font_data = {'fiu_id': id}
	soup = BeautifulSoup(html_str, 'lxml')
	font_img_tag = soup.select('div.gallery-typeface-col1 > img')
	if font_img_tag:
		font_data['name'] = font_img_tag[0].attrs['title']
		font_data['image_url'] = font_img_tag[0].attrs['src']
	font_data['foundries'] = get_family_list(soup, '#family_foundries')
	font_data['designers'] = get_family_list(soup, '#family_designers')
	font_data['related_fonts'] = get_family_list(soup, '#family_related')

	date_tags = soup.select('#family_release_date > ul > li > a')
	if date_tags:
		font_data['date'] = int(date_tags[0].text)

	source_link_tags = soup.select('#family_sources > ul > li > a')
	if source_link_tags:
		font_data['source_links'] = [tag.attrs['href'] for tag in source_link_tags]

	return font_data

def get_family_list(soup, id):
	font_family_items = soup.select(id + ' > ul > li > a > span:nth-of-type(1)')
	return [item.text for item in font_family_items]

def get_editable_list(soup,items):
	selector = '.link-list.editable-list.'+items+' > li > a > span:nth-of-type(1)'
	use_items = soup.select(selector) # needs 'selector' ??

def parse_use_page(html_str,dict):
	use_dict = {}
	typefaces = [] #(to scrape)

	# update fonts_dict
	for font in typefaces:
		fonts_dict['font'] = {}
		fonts_dict['font']['url'] = #to parse

	# soup = ??
	# return one use_dict to append
	use_dict['typefaces'] = typefaces

	font-samples.families.editable-list

	use_dict['formats'] = get_editable_list(soup,'formats')
	use_dict['industries'] = get_editable_list(soup,'industries')
	use_dict['tags'] = get_editable_list(soup,'tags')
	use_dict['location'] = get_editable_list(soup,'location')


# def get_font_page(id):
# 	page_to_get = "http://fontsinuse.com/typefaces/" + str(id)
# 	request = requests.get(page_to_get)
# 	request.raise_for_status()
# 	return request.text



def scrape():
	# font_data_list = []
	# id = 1
	# while True:
	# 	print "fetching font %i" % id
	# 	try:
	# 		page_content = get_font_page(id)
	# 	except requests.exceptions.HTTPError:
	# 		break
	# 	font_data_list.append(parse_font_page(page_content, id))
	# 	id = id + 1
	# with open('fiu_font_data.json', 'w') as outfile:
	# 	json.dump(font_data_list, outfile)


	uses_urls = []
	start_url_list = ['http://fontsinuse.com/collection/'+str(i) for i in range(1,115)]
	for url in start_url_list:
    	webpage = requests.get(url).text
    	soup = BeautifulSoup(webpage, 'lxml')
		for link in soup.findAll("a","gallery-thumb-link"):
        	uses_urls += ['fontsinuse.com'+(link.get('href'))]


    fonts_dict = {}
    use_list = []
    for use_url in uses_urls:
    	html_str = requests.get(use_url).text
    	use_list.append(parse_use_page(html_str,fonts_dict))




if __name__ == '__main__':
	scrape()