# ---------------------------------
# More compatible with python 3 code
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

try:
    range = xrange
except NameError:
    pass

# End of more compatible with python 3
# ---------------------------------

from io import open
import sys
import os

from src.chooser import choose_algorithm, print_algorithms
from src.plotter import plot_graph

DEFAULT_OPTS = "output=detailed;savefile=true;graph=true;filemod="

def print_usage():
    print('Minimum spanning tree solver:')
    print('Usage:')
    print('  python main.py X Y options')
    print()
    print('  where:')
    print('    X is the filename of mst data')
    print('    Y is an integer 1,2,3 ...')
    print('    options are optional added values')
    print('    (default options are {0}'.format(DEFAULT_OPTS))
    print()
    print('  eg python main.py data/tiny.txt 1 "filemod=aha"')
    print()
    print('Available solvers:')
    print_solvers()
    print()


def get_opts():
    # Command line arguments
    algo = sys.argv[2]
    filename = sys.argv[1]
    
    default_opts = {opt.split('=')[0].lower(): opt.split('=')[1].lower() 
        for opt in DEFAULT_OPTS.split(';')} 
    
    if len(sys.argv) > 3:
        opts = sys.argv[3].strip('"')
        opts = {opt.split('=')[0].lower(): opt.split('=')[1].lower() for opt in opts.split(';')}
    else:
        opts = {} 

    opts = dict(default_opts.items() + opts.items())
    return (algo, filename, opts)


def print_results(n_nodes, n_edges, edges, opts, algo_name):
    total_weight = sum([edge[2] for edge in edges])

    if opts['output'] == 'simple':
        print('{0}'.format(total_weight))
    
    elif opts['output'].lower() in ['detailed', 'debug']:
        print('MST {0} algorithm:'.format(algo_name))
        print('Total weight = {0}'.format(total_weight))
        print('Number of nodes = {0}'.format(n_nodes))
        print('Number of edges = {0}'.format(n_edges))


def save_file(n_nodes, n_edges, edges, opts, filename):
    if opts['savefile'] == 'true':
        filename_txt = '{0}.txt'.format(filename)
        with open(filename_txt, 'w') as f:
            f.write('{0}\n'.format(n_nodes))
            f.write('{0}\n'.format(n_edges))
            for edge in edges:
                f.write('{0} {1} {2}\n'.format(edge[0], edge[1], edge[2]))
        if opts['output'] in ['detailed', 'debug']:
            print('Edges saved in {0}'.format(filename_txt))


def save_graph(all_edges, mst_edges, opts, filename):
    if opts['graph'] == 'true':
        file_out = plot_graph(all_edges, mst_edges, filename)
        if opts['output'] in ['detailed', 'debug']:
            print('Graph diagram saved in {0}'.format(file_out))


def main():
    if len(sys.argv) < 3:
        print_usage()
        return

    (algo_choice, file_in, opts) = get_opts()
    Algo = choose_algorithm(algo_choice)

    algo = Algo((opts['graph'] == 'true'))
    algo.set_logging(opts['output'])
    with open(file_in, 'r') as f:
        algo.init_from_file(f)
    (n_nodes, n_edges, edges) = algo.solve()
    
    file_out = 'output/{0}_{1}'.format(os.path.splitext(os.path.basename(file_in))[0], 
        algo.name)
    if opts['filemod']:
        file_out = '{0}_{1}'.format(file_out, opts['filemod'])

    print_results(n_nodes, n_edges, edges, opts, algo.name)
    save_file(n_nodes, n_edges, edges, opts, file_out) 
    save_graph(algo.all_edges, edges, opts, file_out)

if __name__ == '__main__':
    main()
