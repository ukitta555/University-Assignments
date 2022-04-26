from src.utils.computational_types import MyPoint


class PointComparer:
    @staticmethod
    def compare(this: MyPoint, that: MyPoint):
        if this == that:
            return 0
        if this.y > that.y or (this.y == that.y and this.x < that.x):
            return -1
        else:
            return 1