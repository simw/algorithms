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

from src.tspsolver_random import random_solver_once
from src.tspsolver_distanceweighted import distanceweighted_solver_once
from src.utils import tsp_driver

from random import randrange

def edgeswap_solver(tspdata, opts):
    return tsp_driver(edgeswap_solver_once, tspdata, opts) 
    # return edgeswap_solver_once(tspdata, opts)
 
def edgeswap_solver_once(tspdata, opts):
    if opts['base'] == 'distanceweighted':
        (dist, course) = distanceweighted_solver_once(tspdata, opts)
    else:
        (dist, course) = random_solver_once(tspdata, opts)
    
    return single_edge_swapped(dist, course, tspdata, opts)
    # (dist, course) = single_edge_swapped(dist, course, tspdata, opts)
    # return double_edge_swapped(dist, course, tspdata, opts)

def single_edge_swapped(dist, course, tspdata, opts):
    old_dist = 0
    while old_dist != dist:
        old_dist = dist
        # Cut course 0:i, i+1:j, j+1:end
        # Rearrange into 0:i, reversed(i+1:j), j+1:end
        for i in range(1, len(course)-1):
            for j in range(i+1, len(course)):
                new_course = course[:i] + list(reversed(course[i:j])) + course[j:len(course)]
                new_dist = tspdata.course_distance(new_course)

                if new_dist < dist:
                    course = new_course
                    dist = new_dist

    return (dist, course)

def double_edge_swapped(dist, course, tspdata, opts):
    old_dist = 0
    while old_dist != dist:
        old_dist = dist
        # Cut course 0:i, i+1:j, j+1:ii, ii+1:jj, jj+1:end
        # Rearrange into 0:i, reversed(i+1:j), j+1:ii, reversed(ii+1:jj), jj+1:end
        for i in range(1, len(course)-3):
            for j in range(i+1, len(course)-2):
                for ii in range(j+1, len(course)-1):
                    for jj in range(ii+1, len(course)):
                        new_course = (course[:i] + list(reversed(course[i:j])) + 
                                course[j:ii] + list(reversed(course[ii:jj])) + course[jj:len(course)])
                        new_dist = tspdata.course_distance(new_course)

                        if new_dist < dist:
                            course = new_course
                            dist = new_dist

    return (dist, course)

