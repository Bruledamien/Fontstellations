"""Script to transfer data collected about uses (fiu_use_list) into the font dict (fiu_font_dict) as of July 19, 2016
"""

# STEP 1 : for each use,
# - for each font in use, add industries and formats to font dict
# - add a link

from collections import Counter
import json

def create_link_counts():

    with open('fiu_use_list.json') as json_list:
        use_list = json.load(json_list)

    single_link_list = [] # contains all links (a,b) with repetition, and to identify link precisely tuple is 'ordered'

    for use in use_list:
        ordered_typefaces = sorted(use['typefaces'])
        for i in range(1,len(ordered_typefaces)): # nothing if only one font in this use
            single_link_list.append((ordered_typefaces[0],ordered_typefaces[i])) # fonts are ordered in tuple : always (a,b) and never (b,a)

    counter_links = Counter(single_link_list)
    print "Total of " + str(len(counter_links.keys())) + " links in graph"

    graph_links = []
    for key in sorted(counter_links.keys()):
        graph_links.append({"source":key[0], "target": key[1], "value": counter_links[key]})

    with open('graph_links.json', 'w') as outfile:
        json.dump(graph_links, outfile)

def create_font_counts():

    with open('fiu_use_list.json') as json_list:
        use_list = json.load(json_list)

    append_uses = []

    for use in use_list:
        append_uses += use['typefaces']

    counter_obj = Counter(append_uses)
    print "Total of "+str(len(counter_obj.keys()))+" fonts used"

    with open('font_use_counts.json', 'w') as outfile:
        json.dump(counter_obj, outfile)


if __name__ == '__main__':
   #create_font_counts() # goal is to create a Counter object (dict) with "fontname: use-count" as "key: value" pairs.
    create_link_counts() # goal is to create a Counter Object (dict) with "(font1,font2): count" pairs