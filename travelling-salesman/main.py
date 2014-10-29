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

from src.tspdata import TspData
from src.tspplotter import plot_path
from src.tspsolvers import choose_solver, print_solvers

DEFAULT_OPTS = "output=detailed;graph=true;n=1;dnorm=1;dexp=10;pexp=5;pdecay=0.95;base=random;filemod="

def main():
    if len(sys.argv) < 3:
        print_usage()
        return

    # Command line arguments
    algo = sys.argv[1]
    filename = sys.argv[2]
    
    default_opts = {opt.split('=')[0].lower(): opt.split('=')[1].lower() 
        for opt in DEFAULT_OPTS.split(';')} 
    
    if len(sys.argv) > 3:
        opts = sys.argv[3].strip('"')
        opts = {opt.split('=')[0].lower(): opt.split('=')[1].lower() for opt in opts.split(';')}
    else:
        opts = {} 

    opts = dict(default_opts.items() + opts.items())

    # Run the solver
    with open(filename, 'r') as f:
        data = TspData(f)
    (solver, name, filename_out) = choose_solver(algo)
    (travelled, course) = solver(data, opts)

    # Output results
    if opts['output'].lower() == 'detailed':
        print('TSP {0} algorithm:'.format(name))
        print('Distance = {0}'.format(travelled))
        print('Course = {0}'.format(course))

    elif opts['output'] == 'simple':
        print('{0}'.format(travelled))

    filename = os.path.splitext(os.path.basename(filename))[0]
    filename = '{0}_{1}'.format(filename, filename_out)
    if opts['filemod']:
        filename = '{0}_{1}'.format(filename, opts['filemod'])
    if opts['graph'] == 'true':
        filename = plot_path(data, course, filename)
        if opts['output'] == 'detailed':
            print('Course diagram saved in {0}'.format(filename))

def print_usage():
    print('Travelling salesman solver')
    print('Usage:')
    print('  python main.py X Y options')
    print()
    print('  where:')
    print('    X is an integer 1,2,3 ...')
    print('    Y is the filename of tsp data')
    print('    options are optional added values')
    print('    (default options are {0}'.format(DEFAULT_OPTS))
    print()
    print('  eg python main.py 1 tspdata.tsp "n=1000;r=10;norm=500;rp=2"')
    print()
    print('Available solvers:')
    print_solvers()
    print()

if __name__ == '__main__':
    main()
