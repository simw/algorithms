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

from src.utils import weighted_choice
from src.utils import tsp_driver

def distanceweighted_solver(tspdata, opts):
    n = int(opts['n'])
    return tsp_driver(distanceweighted_solver_once, tspdata, opts)

def distanceweighted_solver_once(tspdata, opts):
    distance_exponent = int(opts['dexp'])
    distance_norm = int(opts['dnorm'])
    
    point = 0
    course = [point]
    points_remaining = list(range(1, len(tspdata)))

    while len(points_remaining) > 0:
        distances = tspdata.all_dists(point)
        weights = [distance_function(distances[i], distance_exponent, distance_norm) 
                for i in points_remaining]
        point = weighted_choice(points_remaining, weights)
        course.append(point)
        points_remaining.remove(point)

    travelled = tspdata.course_distance(course)

    return (travelled, course)

def distance_function(dist, distance_exponent, distance_norm):
    return (distance_norm / dist)**distance_exponent

