"""Script for testing stuff in console
"""

import json

# sorted fonts in fonts_dict
# with open('fiu_fonts_dict.json') as dict_json:
#     fonts_dict = json.load(dict_json)
#
# ordered_fonts = sorted(fonts_dict.keys())
#
# with open('ordered_fonts.json','w') as outfile:
#     json.dump(ordered_fonts,outfile)


# compare ordered list of fonts for links and nodes

links_fonts = []
with open('../ForceGraph/graph_links_2.json') as links_json:
    link_list = json.load(links_json)

for link in link_list:
    source = link["source"]
    target = link["target"]

    if not (source in links_fonts):
        links_fonts.append(source)

    if not (target in links_fonts):
        links_fonts.append(target)

links_fonts = sorted(links_fonts)

with open('../ForceGraph/graph_nodes_2.json') as nodes_json:
    nodes_list = json.load(nodes_json)

nodes_fonts = []
for node in nodes_list:
    print node
    print "\n"
    nodes_fonts.append(node["name"])

nodes_fonts = sorted(nodes_fonts)

print "list are the same : " + str(nodes_fonts == links_fonts)

for font in links_fonts:
    if font not in nodes_fonts:
        print "font not in nodes: " + font

with open('ordered_links_fonts.json','w') as outfile:
    json.dump(links_fonts,outfile)

with open('ordered_nodes_fonts.json','w') as outfile:
    json.dump(nodes_fonts,outfile)

