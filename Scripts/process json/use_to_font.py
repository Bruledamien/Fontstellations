
from collections import Counter
import json

# counts how many times a given link existed in uses, independently of order of two nodes
def create_link_counts():

    with open('fiu_use_list.json') as json_list:
        use_list = json.load(json_list)

    single_link_list = []  # contains all links (a,b) with repetition, and to identify link precisely tuple is 'ordered'

    for use in use_list:
        ordered_typefaces = sorted(use['typefaces'])
        for i in range(1, len(ordered_typefaces)):  # nothing if only one font in this use
            # fonts are ordered in tuple : always (a,b) and never (b,a)
            single_link_list.append((ordered_typefaces[0], ordered_typefaces[i]))

    counter_links = Counter(single_link_list)
    print "Total of " + str(len(counter_links.keys())) + " links in graph"

    # convert Counter for export and d3 format
    graph_links = []
    for key in sorted(counter_links.keys()):
        graph_links.append({"source": key[0], "target": key[1], "value": counter_links[key]})

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


def augment_dict_and_create_nodes():

    with open('fiu_use_list.json') as json_list:
        use_list = json.load(json_list)

    with open('font_use_counts.json') as counts:
        counts_dict = json.load(counts)

    with open('fiu_fonts_dict_augmented.json') as dict:
        fonts_dict = json.load(dict)

    for use in use_list:
        for typeface in use['typefaces']:
            fonts_dict[typeface]["industries"] = use["industries"]
            fonts_dict[typeface]["formats"] = use["formats"]
            fonts_dict[typeface]["uses"] = counts_dict[typeface]

    nodes_list = []

    for key in fonts_dict.keys():
        nodes_list.append(fonts_dict[key])

    with open('graph_nodes.json','w') as outfile:
        json.dump(nodes_list,outfile)


            # new_type_dict = fonts_dict['typeface']
            # new_type_dict["industries"] = use["industries"]
            # new_type_dict["formats"] = use["formats"]
            # fonts_dict['typeface'] = new_type_dict


if __name__ == '__main__':
   #create_font_counts() # goal is to create a Counter object (dict) with "fontname: use-count" as "key: value" pairs.
   #create_link_counts() # goal is to create a Counter Object (dict) with "(font1,font2): count" pairs
   augment_dict_and_create_nodes() # goal is to augment current font_dict_augmented with new info from font_use_counts