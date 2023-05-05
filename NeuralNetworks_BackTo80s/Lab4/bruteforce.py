import utils
import numpy as np
import itertools


def shortestPaths(distance_matrix):
    shortest_path_distance = None
    shortest_paths = [] # track all valid paths with best distance

    paths = itertools.permutations(range(distance_matrix.shape[0]))

    for curPath in paths:
        # revisit the first node at the end of the route
        curPath = list(curPath) + [curPath[0]]

        pathDistance = utils.pathDistance(distance_matrix, curPath)

        if shortest_path_distance is None or pathDistance < shortest_path_distance:
            shortest_path_distance = pathDistance

            # we found a better candidate, delete all solutions tracked
            shortest_paths = []

        if pathDistance == shortest_path_distance:
            shortest_paths.append(curPath)

    return shortest_paths


def longestPath(distance_matrix):
    longest_path = None
    longest_path_distance = None

    paths = itertools.permutations(range(distance_matrix.shape[0]))

    for curPath in paths:
        # revisit the first node at the end of the route
        curPath = list(curPath) + [curPath[0]]

        pathDistance = utils.pathDistance(distance_matrix, curPath)

        if longest_path_distance is None or pathDistance > longest_path_distance:
            longest_path = curPath
            longest_path_distance = pathDistance

    return [longest_path]