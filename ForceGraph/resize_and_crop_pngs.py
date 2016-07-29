'''
Script to resize pngs to a smaller/compressed size as of July 22, 2016.
'''

import os
from PIL import Image
import sys

path = "font_pngs" # path to pngs dir

list_of_files = os.listdir(path)
for i in range(1, len(list_of_files)): # element at 0 is DS_Store

    current_file = os.path.join(path,list_of_files[i])
    img = Image.open(current_file)
    size = img.size


    #resize
    if size[0] > 300: # prevent from rezising img twice, since original png is approx 800x200
        img = img.resize((size[0]/4,size[1]/4), Image.ANTIALIAS)
        new_size = img.size
        print list_of_files[i] + " #" + str(i) + "of size :" + str(size)+ " is now: " +str(new_size)

    # crop out transparent parts
    imgbox = img.getbbox()
    img = img.crop(imgbox)
    img.save(current_file, optimize=True, quality=95)