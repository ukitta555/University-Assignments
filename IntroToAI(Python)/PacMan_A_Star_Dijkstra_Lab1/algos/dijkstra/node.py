import functools

from util import LabyrinthLocation


@functools.total_ordering
class Node:
    def __init__(self, i, j, dist, path):
        self.i = i
        self.j = j
        self.dist = dist
        self.path = path

    def __lt__(self, other):
        return self.dist < other.dist

    def __eq__(self, other):
        return self.dist == other.dist

    def adj(self, height, width):
        result = []
        if self.i >= 1:
            result.append(LabyrinthLocation(i=self.i-1, j=self.j))
        if self.i < height - 1:
            result.append(LabyrinthLocation(i=self.i+1, j=self.j))
        if self.j >= 1:
            result.append(LabyrinthLocation(i=self.i, j=self.j-1))
        if self.j < width - 1:
            result.append(LabyrinthLocation(i=self.i, j=self.j+1))
        return result
    