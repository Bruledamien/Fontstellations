"""Script for scraping information from fontsinuse.com as of July 19, 2016
"""

import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
import time


def parse_font_page(name, id, dict):

    font_data = {"url_id":id}
    html_str = requests.get('http://fontsinuse.com/typefaces/' + str(id)).text  # careful
    soup = BeautifulSoup(html_str, 'lxml')
    font_img_tag = soup.select('div.gallery-typeface-col1 > img')
    if font_img_tag:
        font_data['name'] = font_img_tag[0].attrs['title'] # this should be the same as the previously scraped name
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

    dict[name] = font_data

    pprint(dict)

    with open('fiu_fonts_dict_augmented.json', 'w') as outfile:
        json.dump(dict, outfile)


def get_family_list(soup, id):
    font_family_items = soup.select(id + ' > ul > li > a > span:nth-of-type(1)')
    return [item.text for item in font_family_items]

def scrape_font_data():

        with open('fiu_fonts_dict.json') as json_file:
            fonts_dict = json.load(json_file)

        fonts_list = fonts_dict.keys() #same list will be used to scrape fonts, since the file will not be modified by this script

        print len("number of fonts: " + str(fonts_list))

        # set start index for scraping
        start_index = 0

        if start_index > 0:  # ie we have already saved an augmented fonts dict
            with open('fiu_fonts_dict_augmented.json') as json_dict:
                fonts_dict_aug = json.load(json_dict)

        else:
            fonts_dict_aug = {} # creating a new dict by precaution; we will save augmented dict to new file

        for i in range(start_index, len(fonts_list)):
            font_name = fonts_list[i]
            url_id = fonts_dict[font_name]["url_id"]  # fonts_dict[font_name] is a dict

            print "fetching url " + str(i) + " ; with id " + str(url_id) + "\n"
            parse_font_page(font_name, url_id, fonts_dict_aug)

if __name__ == '__main__':
    scrape_font_data()