import copy
import heapq

import numpy as np

from algos.dijkstra.node import Node
from tile import Tile
from tile_enum import TileEnum
from util import LabyrinthLocation

def run_dijkstra(
        ghost_location: LabyrinthLocation,
        target: LabyrinthLocation,
        labyrinth: list[list[Tile]],
):
    heap = []
    labyrinth_visited: list[list[bool]] = []
    labyrinth_weights: list[list[int]] = []
    labyrinth_shortest_paths: list[list[list[LabyrinthLocation] | None]] = []
    for i, line in enumerate(labyrinth):
        labyrinth_visited.append([])
        labyrinth_weights.append([])
        labyrinth_shortest_paths.append([])
        for tile in line:
            if tile.tile_type is TileEnum.WALL:
                labyrinth_visited[i].append(True)
            else:
                labyrinth_visited[i].append(False)
            labyrinth_weights[i].append(np.Infinity)
            labyrinth_shortest_paths[i].append(None)
    labyrinth_weights[ghost_location.i][ghost_location.j] = 0
    heapq.heappush(heap, Node(ghost_location.i, ghost_location.j, 0, []))
    while len(heap) > 0:
        min_dist_node = heapq.heappop(heap)
        labyrinth_visited[min_dist_node.i][min_dist_node.j] = True
        for adj_location in min_dist_node.adj(
                height=len(labyrinth_visited),
                width=len(labyrinth_visited[0])
        ):
            if not labyrinth_visited[adj_location.i][adj_location.j]:
                if labyrinth_weights[adj_location.i][adj_location.j] > min_dist_node.dist + 1:
                    labyrinth_weights[adj_location.i][adj_location.j] = min_dist_node.dist + 1
                path_copy = copy.deepcopy(min_dist_node.path)
                path_copy.append(LabyrinthLocation(min_dist_node.i, min_dist_node.j))
                heapq.heappush(
                    heap,
                    Node(
                        i=adj_location.i,
                        j=adj_location.j,
                        dist=labyrinth_weights[adj_location.i][adj_location.j],
                        path=path_copy
                    )
                )
                labyrinth_shortest_paths[adj_location.i][adj_location.j] = path_copy
    labyrinth_shortest_paths[target.i][target.j].append(LabyrinthLocation(target.i, target.j))
    return labyrinth_shortest_paths[target.i][target.j]