"""Script for scraping information from fontsinuse.com as of June 24, 2016
"""

import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
import time


def get_family_list(soup, id):
    font_family_items = soup.select(id + ' > ul > li > a > span:nth-of-type(1)')
    return [item.text for item in font_family_items]

def get_editable_list(soup,items):
    selector = '.link-list.editable-list.'+items+' > li > a > span:nth-of-type(1)'
    use_items = soup.select(selector) # needs 'selector' ??
    return [item.text for item in use_items]

def parse_use_page(url,fonts_dict,use_list):

    use_dict = {}
    html_str = requests.get('http://' + url).text  # careful
    soup = BeautifulSoup(html_str, 'lxml')
    typeface_elements = soup.select('.font-samples.families.editable-list > li > a')
    typefaces = []

    # update fonts_dict and typefaces
    for element in typeface_elements:
        font = element.select('img')[0].attrs['title']
        typefaces.append(font)
        fonts_dict[font] = {}
        fonts_dict[font]['url_id'] = int(element.attrs['href'].rsplit('/')[2])

    # return one use_dict to append
    use_dict['fiu_id'] = int(url.rsplit('/')[2]) #take id out of url of type "http://fontsinuse.com/uses/13632/name"
    use_dict['typefaces'] = typefaces
    use_dict['formats'] = get_editable_list(soup,'formats')
    use_dict['industries'] = get_editable_list(soup,'industries')
    use_dict['tags'] = get_editable_list(soup,'tags')
    use_dict['location'] = get_editable_list(soup,'location')

    use_list.append(use_dict)

    # pprint(use_dict)
    # print '\n'
    # pprint(fonts_dict)

    with open('fiu_fonts_dict.json', 'w') as outfile:
        json.dump(fonts_dict, outfile)

    with open('fiu_use_list.json', 'w') as outfile:
        json.dump(use_list, outfile)


# def get_font_page(id):
# 	page_to_get = "http://fontsinuse.com/typefaces/" + str(id)
# 	request = requests.get(page_to_get)
# 	request.raise_for_status()
# 	return request.text


def scrape_font_data():

    with open('uses_urls.json') as json_file:
        uses_urls = json.load(json_file)

    print len(uses_urls)

    # set start index for scraping
    start_index = 447

    if start_index > 0: # ie we have already saved some files
        with open('fiu_fonts_dict.json') as json_dict:
            fonts_dict = json.load(json_dict)

        with open('fiu_use_list.json') as json_list:
            use_list = json.load(json_list)
    else :
        fonts_dict = {}
        use_list = []

    for i in range(start_index,len(uses_urls)):
        print "fetching url "+str(i)+" : "+str(uses_urls[i]) + "\n"
        parse_use_page(uses_urls[i], fonts_dict, use_list)


# TO DO NEXT 
# - enable file to be written / modified several times (NOT rewriting whole file each time...)
# - combine this with a feature to crawl urls and save position in list / restart later

if __name__ == '__main__':
    scrape_font_data()