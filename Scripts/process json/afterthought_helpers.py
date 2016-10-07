'''
Goal is to reduce graph_nodes files because I don't need the source_links
'''

import json


def delete_source_links():
    with open("../../ForceGraph/Data/absolute link value/graph_nodes_cleaned.json") as nodes:
        graph_nodes = json.load(nodes)
    for node in graph_nodes:
        node.pop("source_links", None)
        node.pop("related_fonts", None)

    with open("../../ForceGraph/Data/absolute link value/graph_nodes_cleaned_lite.json", 'w') as outfile:
            json.dump(graph_nodes, outfile)

# note efficient...
def compute_number_of_pairs():
    with open("../../ForceGraph/Data/absolute link value/graph_nodes_cleaned_lite.json") as nodes:
        graph_nodes = json.load(nodes)

    with open("../../ForceGraph/Data/absolute link value/graph_links_cleaned.json") as links:
        graph_links = json.load(links)

    for node in graph_nodes:
        node_pairs = 0
        for link in graph_links:
            if link['source'] == node['name'] or link['target'] == node['name']:
                node_pairs += link['value']

        node['single_couses'] = node_pairs

    with open("../../ForceGraph/Data/absolute link value/graph_nodes_cleaned_lite.json", 'w') as outfile:
        json.dump(graph_nodes, outfile)


if __name__ == '__main__':
    delete_source_links()
    compute_number_of_pairs()
