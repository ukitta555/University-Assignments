from src.utils.computational_types import MySegment, SortedSet


class LCUEvent:
    def __init__(self):
        self.lower: SortedSet[MySegment] = SortedSet()
        self.contains: SortedSet[MySegment] = SortedSet()
        self.upper: SortedSet[MySegment] = SortedSet()

    def add_to_L(self, segment: MySegment):
        self.lower.insert(segment)

    def add_to_C(self, segment: MySegment):
        self.contains.insert(segment)

    def add_to_U(self, segment: MySegment):
        self.upper.insert(segment)
