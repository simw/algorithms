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
from src.tspsolver_edgeswap import single_edge_swapped 

def antcolony_solver(tspdata, opts):
    n = int(opts['n'])
    distance_exponent = float(opts['dexp'])
    distance_norm = float(opts['dnorm'])
    pheromone_exponent = float(opts['pexp'])
    pheromone_decay = float(opts['pdecay'])

    d = len(tspdata)

    # pheromone[i][j]: on path from node i to node j
    pheromones = [[0 for i in range(d)] for j in range(d)]
    min_travelled = -1

    for i in range(n):
        # New ant!
        point = 0
        course = [point]
        points_remaining = list(range(1, d))

        while len(points_remaining) > 0:
            dists = tspdata.all_dists(point)
            weights = [distance_function(dists[i], distance_exponent, distance_norm) 
                    for i in points_remaining]
            weights = [weights[i] * (1 + 
                    pheromones[point][points_remaining[i]]) for i in range(len(weights))]
            point = weighted_choice(points_remaining, weights)

            course.append(point)
            points_remaining.remove(point)

         
        travelled = tspdata.course_distance(course)
        (travelled, course) = single_edge_swapped(travelled, course, tspdata, opts) 
        if i == 0:
            pheromone_norm = travelled

        if travelled < min_travelled or min_travelled < 0:
            min_travelled = travelled
            min_course = course

        # Decay pheromones
        pheromones = [[pheromones[i][j]*pheromone_decay for i in range(d)] for j in range(d)]

        # Add pheromones
        for i in range(len(course)-1):
            pheromones[course[i]][course[i+1]] += (pheromone_norm / travelled)**pheromone_exponent

    return (min_travelled, min_course)

def distance_function(dist, distance_exponent, distance_norm):
    return (distance_norm / dist)**distance_exponent

