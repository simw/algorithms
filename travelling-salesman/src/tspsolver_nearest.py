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

def nearest_solver(tspdata, dummy):
    point = 0
    course = [point]
    points_remaining = list(range(1, len(tspdata)))
    travelled = 0

    while len(points_remaining) > 0:
        (point, next_dist) = filtered_min(tspdata.all_dists(point),
            points_remaining)

        # travelled = travelled + next_dist 
        points_remaining.remove(point)
        course.append(point)

    travelled = tspdata.course_distance(course)
    return (travelled, course)


def filtered_min(list_in, filter_list):
    filtered_list = [list_in[i] for i in filter_list]
    min_value = min(filtered_list)
    min_index = filter_list[filtered_list.index(min_value)]

    return (min_index, min_value)

