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

from random import uniform
from bisect import bisect

def weighted_choice(choices, weights):
    total = 0
    cumulative_weights = []
    for weight in weights:
        total = total + weight
        cumulative_weights.append(total)

    r = uniform(0, total)
    i = bisect(cumulative_weights, r)
    return choices[i]

def tsp_driver(solver, tspdata, opts):
    num_iterations = int(opts['n'])
    (min_travelled, best_course) = solver(tspdata, opts)
    for i in range(1, num_iterations):
        (travelled, course) = solver(tspdata, opts)
        if  travelled < min_travelled:
            min_travelled = travelled
            best_course = course

    return (min_travelled, best_course)

