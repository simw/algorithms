from __future__ import unicode_literals
from __future__ import absolute_import

from src.tspsolver_random import random_solver 
from src.tspsolver_nearest import nearest_solver
from src.tspsolver_insertion import insertion_solver
from src.tspsolver_edgeswap import edgeswap_solver
from src.tspsolver_distanceweighted import distanceweighted_solver
from src.tspsolver_antcolony import antcolony_solver

solvers = {
    '1': {
        'name': 'Random',
        'filename': 'random',
        'fn': random_solver
    },
    '2': {
        'name': 'Nearest neighbour',
        'filename': 'nearest',
        'fn': nearest_solver
    },
    '3': {
        'name': 'Insertion',
        'filename': 'insertion',
        'fn': insertion_solver
    },
    '4': {
        'name': 'Edge swap',
        'filename': 'edgeswap',
        'fn': edgeswap_solver
    },
    '5': {
        'name': 'Distance weighted',
        'filename': 'distanceweighted',
        'fn': distanceweighted_solver
    },
    '6': {
        'name': 'Ant colony',
        'filename': 'antcolony',
        'fn': antcolony_solver
    }

}

def choose_solver(choice):
    choice = '{0}'.format(choice).strip()
    res = solvers[choice]

    return (res['fn'], res['name'], res['filename'])

def print_solvers():
    for i in range(100):
        k = '{0}'.format(i)
        if k in solvers:
            print('  {0}: {1}'.format(i, solvers[k]['name']))
