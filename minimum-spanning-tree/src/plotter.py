from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division

import matplotlib.pyplot as plt
import networkx as nx

def plot_graph(all_edges, highlighted_edges, filename):
    all_edge_labels = {(v[0], v[1]): v[2] for v in all_edges}
    highlighted_edge_labels = {(v[0], v[1]): v[2] for v in highlighted_edges}

    all_edges = [(e[0], e[1], 1/e[2]) for e in all_edges]

    g = nx.Graph()
    g.add_weighted_edges_from(all_edges)
    pos = nx.spring_layout(g)

    nx.draw(g, pos, with_labels=True, edge_color='0.75')
    nx.draw(g, pos, edge_color='0', edgelist=highlighted_edges)
    
    nx.draw_networkx_edge_labels(g, pos, edge_labels=all_edge_labels, 
        font_color='0.75')
    nx.draw_networkx_edge_labels(g, pos, edge_labels=highlighted_edge_labels, 
        font_color='0')

    plt.axis('off')
    plt.title('Graph')
    plt.show()
    filename_out = '{0}.png'.format(filename)
    plt.savefig(filename_out)
    plt.close()

    return filename_out
