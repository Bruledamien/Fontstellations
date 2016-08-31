'''
Script to resize pngs to a smaller/compressed size as of Aug 12, 2016.
'''

import os
from PIL import Image, ImageOps
import json
from math import floor

with open('graph_nodes_cleaned.json') as json_file:
    nodes = json.load(json_file)

    path = "font_pngs_original_cleaned"  # path to pngs dir

for (i, node) in enumerate(nodes):

    current_file = os.path.join(path, node['image_url'])
    img = Image.open(current_file)
    size = img.size

    img = img.convert("RGBA")

    # invert black into white
    # r, g, b, a = img.split()
    # rgb_image = Image.merge('RGB', (r, g, b))
    # inverted_image = ImageOps.invert(rgb_image)
    #
    # r2, g2, b2 = inverted_image.split()
    # img = Image.merge('RGBA', (r2, g2, b2, a))

    # # delete black background and make it transparent
    # data = img.getdata()
    #
    # new_data = []
    # for datum in data:
    #     if 200 > datum[0] and 200 > datum[1] and 200 > datum[2]:
    #         new_data.append((255, 255, 255, 0))
    #     else:
    #         new_data.append(datum)

    # OR delete white background and make it transparent
    data = img.getdata()

    new_data = []
    for datum in data:
        if 100 < datum[0] and 100 < datum[1] and 100 < datum[2]:
            new_data.append((255, 255, 255, 0))
            # improvment would involve keeping grayscales and setting transparency according to saturation.
        else:
            new_data.append(datum)

    img.putdata(new_data)
    print node['name'] + " #" + str(i) + " saved"

    img.save(current_file, optimize=True, quality=99)
