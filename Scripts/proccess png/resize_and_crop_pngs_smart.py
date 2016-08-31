'''
Script to resize pngs to a smaller/compressed size as of August 13, 2016.
'''

import json
import os
from math import floor
from PIL import Image


# Careful : this version is based on the graph_node_2 file and can lead to errors if files missing in path dir.
# previous version of script just processes list of files in a particular folder

with open('graph_nodes_cleaned.json') as json_file:
    nodes = json.load(json_file)

    path = "originals_cleaned_scaled"  # path to pngs dir

for (i, node) in enumerate(nodes):

    current_file = os.path.join(path, node['image_url'])
    img = Image.open(current_file)
    size = img.size

    #  resize according to importance in graph
    #  uses range from 1 to 348 -- we want scale to be ~ 1/4 -- 1

    factor = 0.002 * node['uses'] + 0.248  # linear transform
    print node['name'] + " : factor = " + str(factor)

    if size[0] > 900 * factor:  # prevent from rezising img twice, since original png is approx 800x200
        print node['name'] + " : size[0] = " + str(int(floor(size[0] / factor))) + '\n'
        img = img.resize((int(floor(size[0] * factor)), int(floor(size[1] * factor))), Image.ANTIALIAS)
        new_size = img.size
        print node['name'] + " #" + str(i) + " of size :" + str(size) + " is now: " + str(new_size)

    # crop out transparent parts
    imgbox = img.getbbox()
    img = img.crop(imgbox)

    print node['name'] + " #" + str(i) + " saved"

    img.save(current_file, optimize=True, quality=99)