from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division

import matplotlib.pyplot as plt
import networkx as nx

def plot_path(tspdata, path, name):
    g = nx.Graph()
    g.add_nodes_from(range(len(tspdata.coords)))

    edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
    g.add_edges_from(edges)

    pos = {}
    label_pos = {}
    for i in range(len(tspdata.coords)):
        pos[i] = (tspdata.coords[i][0], tspdata.coords[i][1])
        label_pos[i] = (pos[i][0], pos[i][1])

    nx.draw_networkx_nodes(g, pos, node_size=10)
    nx.draw_networkx_edges(g, pos, alpha=0.5, width=1)
    nx.draw_networkx_labels(g, label_pos, font_size=8)

    plt.axis('off')
    plt.title('{0}: distance = {1}'.format(name, tspdata.course_distance(path)))
    filename = 'output/{0}.png'.format(name)
    plt.savefig(filename)
    plt.close()
    # plt.show()

    return filename
