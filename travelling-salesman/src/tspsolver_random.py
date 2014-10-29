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

from random import sample
from src.utils import tsp_driver

def random_solver(tspdata, opts):
    return tsp_driver(random_solver_once, tspdata, opts)

def random_solver_once(tspdata, dummy):
    course = [0] + sample(range(1, len(tspdata)), len(tspdata)-1)
    travelled = tspdata.course_distance(course)
    return (travelled, course)

