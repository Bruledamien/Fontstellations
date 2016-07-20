"""Script for testing stuff in console
"""

import json

with open('fiu_fonts_dict.json') as dict_json:
    fonts_dict = json.load(dict_json)

ordered_fonts = sorted(fonts_dict.keys())

with open('ordered_fonts.json','w') as outfile:
    json.dump(ordered_fonts,outfile)

