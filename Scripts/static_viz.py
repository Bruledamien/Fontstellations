"""Use networkx / graphviz to make a quick static graph called
'graph.svg' with a given treshold on the required number of
co-occurences to include. Use it like:

>>> python static_viz.py 2

to only include links between fonts that have occured together 2 or
more times.

"""
import json
import sys

import networkx as nx

import pygraphviz


def read_jsons(nodes_filename, links_filename):

    with open(nodes_filename) as infile:
        nodes = json.load(infile)

    with open(links_filename) as infile:
        links = json.load(infile)

    return nodes, links


def create_graph(nodes, links, threshold):

    # draw directed graph with orthogonal edge routing
    graph = nx.Graph()

    for node in nodes:
        graph.add_node(node['name'])

    # add edges to graph
    for link in links:
        if int(link['value']) >= threshold:
            graph.add_edge(link['source'], link['target'])

    # get rid of this one
    graph.remove_node('unidentified typeface')

    ordered = []
    for node_set in nx.connected_components(graph):
        ordered.append((len(node_set), node_set))

    ordered.sort(reverse=True)

    for size, node_set in ordered[1:]:
        for name in node_set:
            graph.remove_node(name)

    return graph


def format_graph(graph):
    graph.graph_attr['overlap'] = 'false'
    graph.graph_attr['stylesheet'] = 'style.css'
    graph.graph_attr['splines'] = 'false'
    graph.graph_attr['bgcolor'] = 'transparent'
    graph.graph_attr['outputorder'] = 'edgesfirst'
    graph.node_attr['style'] = 'filled'
    graph.node_attr['shape'] = 'ellipse'
    graph.node_attr['margin'] = '0.01, 0.01'
    graph.node_attr['width'] = '0.0'
    graph.node_attr['height'] = '0.0'


def main(nodes_filename, links_filename, treshold):

    # read jsons
    nodes, links = read_jsons(nodes_filename, links_filename)

    # make a graph using network x
    nx_graph = create_graph(nodes, links, threshold=treshold)

    # convert to graphviz for drawing
    gv_graph = nx.nx_agraph.to_agraph(nx_graph)

    # set format
    format_graph(gv_graph)

    # prog=neato|dot|twopi|circo|fdp|nop
    gv_graph.draw("graph.svg", prog='neato')


if __name__ == '__main__':

    threshold = int(sys.argv[1])
    nodes_filename = \
        '../ForceGraph/Data/absolute link value/graph_nodes_min0.json'
    links_filename = \
        '../ForceGraph/Data/absolute link value/graph_links_min0.json'
    main(nodes_filename, links_filename, threshold)
