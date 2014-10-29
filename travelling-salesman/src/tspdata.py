from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division

from math import sqrt

class TspData(object):
    def __init__(self, f=None, force_integer=False):
        if f:
            self.import_data(f, force_integer)

    def import_data(self, f, force_integer=False):
        self.coords = []
        self.force_integer = force_integer

        is_data = False
        for line in f:
            if is_data:
                words = line.split()
                if len(words) == 3:
                    self.coords.append((float(words[1]), float(words[2])))

            elif line.strip() == "NODE_COORD_SECTION":
                is_data = True

        self.coords_to_distances(self.coords, force_integer)

    def coords_to_distances(self, coords, force_integer=False):
        self.distances = []
        for i in range(len(coords)):
            self.distances.append([])
            for j in range(len(coords)):
                d2 = (coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2
                d = sqrt(d2)
                if force_integer:
                    d = int(d)
                self.distances[i].append(d)

    def __len__(self):
        return len(self.distances)

    def dist(self, i, j):
        return self.distances[i][j]

    def all_dists(self, i):
        return self.distances[i][:]

    def course_distance(self, course, return_home=True):
        res = 0
        for i in range(len(course)-1):
            res = res + self.dist(course[i], course[i+1])
        if return_home: 
            res = res + self.dist(course[len(course)-1], course[0])

        return res

