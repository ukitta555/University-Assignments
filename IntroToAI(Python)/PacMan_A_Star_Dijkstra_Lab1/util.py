class LabyrinthLocation:
    def __init__(self, i: int = -1, j: int = -1):
        self.i = i
        self.j = j

    def update_location(self, delta_i, delta_j):
        self.i += delta_i
        self.j += delta_j

    def manhattan_distance(self, other):
        return abs(self.i - other.i) + abs(self.j - other.j)
