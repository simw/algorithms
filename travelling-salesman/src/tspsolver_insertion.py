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

def insertion_solver(tspdata, dummy):
    point = 0
    course = [point]
    points_remaining = list(reversed(range(1, len(tspdata))))
    travelled = 0

    while len(points_remaining) > 0:
        new_min_distance = -1
        for point in points_remaining:
            for i in range(1, len(course)+1):
                if i == len(course):
                    old_subcourse = [course[i-1], course[0]]
                    new_subcourse = [course[i-1], point, course[0]]
                else:
                    old_subcourse = [course[i-1], course[i]]
                    new_subcourse = [course[i-1], point, course[i]]

                change_in_dist = (tspdata.course_distance(new_subcourse, False) - 
                    tspdata.course_distance(old_subcourse, False))

                if new_min_distance < 0 or change_in_dist < new_min_distance:
                    new_min_point = point
                    new_min_position = i
                    new_min_distance = change_in_dist

        course.insert(new_min_position, new_min_point)
        travelled = travelled + new_min_distance
        points_remaining.remove(new_min_point)

    return (travelled, course)

# def insertion_solver_old(tspdata, dummy):
#     point = 0
#     course = [point]
#     points_remaining = list(reversed(range(1, len(tspdata))))
#     travelled = 0
# 
#     while len(points_remaining) > 0:
#         new_min_distance = -1
#         for point in points_remaining:
#             for i in range(1, len(course)+1):
#                 new_course = course[:]
#                 new_course.insert(i, point)
#                 new_distance = tspdata.course_distance(new_course)
# 
#                 if new_min_distance < 0 or new_distance < new_min_distance:
#                     new_min_distance = new_distance
#                     new_min_course = new_course
#                     new_min_point = point
# 
#         course = new_min_course
#         travelled = new_min_distance
#         points_remaining.remove(new_min_point)
#     return (travelled, course)

