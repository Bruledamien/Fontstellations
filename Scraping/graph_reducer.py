'''
Goal is to reduce the graph_nodes and graph_links to visualize quickly
'''

import json

with open("../ForceGraph/graph_links_2.json") as links:
    graph_links = json.load(links)

with open("../ForceGraph/graph_nodes_2.json") as nodes:
    graph_nodes = json.load(nodes)

authorized_fonts_list = [node["name"] for node in graph_nodes if node['uses'] > 20]
authorized_nodes = [node for node in graph_nodes if node['uses'] > 10 ]

print authorized_fonts_list
print str(len(authorized_fonts_list)) + " authorized fonts"

authorized_links = [link for link in graph_links if (link['source'] in authorized_fonts_list and link['target'] in authorized_fonts_list)]

print ("Helvetica" in authorized_fonts_list and "Futura" in authorized_fonts_list)
print str(len(authorized_links)) + " authorized links"

with open("../ForceGraph/graph_links_reduced.json",'w') as outfile:
        json.dump(authorized_links, outfile)

with open("../ForceGraph/graph_nodes_reduced.json",'w') as outfile:
        json.dump(authorized_nodes, outfile)