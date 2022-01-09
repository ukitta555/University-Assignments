import typing

from PyQt5 import QtGui, QtCore, Qt
from PyQt5.QtCore import QLineF
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsLineItem
from sympy import Point2D, Segment2D


class DrawingBoardScene(QGraphicsScene):
    def addSegment(self, line: QtCore.QLineF, pen: typing.Union[QtGui.QPen, QtGui.QColor, QtCore.Qt.GlobalColor,
                                                                QtGui.QGradient] = QtGui.QPen(Qt.Qt.black)) -> \
            QGraphicsLineItem:
        return super().addLine(line, pen)


class Segment(Segment2D):
    def __eq__(self, other):
        one_way = self.p1 == other.p1 and self.p2 == other.p2
        another = self.p1 == other.p2 and self.p2 == other.p1
        return one_way or another


class Point2D(Point2D):
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

RawSegment: typing.TypeAlias = tuple[float, float, float, float]


class QtSegment(QLineF):
    def __eq__(self, other):
        x1 = self.x1() == other.x1()
        x2 = self.x2() == other.x2()
        y1 = self.y1() == other.y1()
        y2 = self.y2() == other.y2()
        return x1 and x2 and y1 and y2

    def __str__(self):
        return f"({self.x1()} {self.y1()} {self.x2()} {self.y2()})"


class SegmentForMockFile(QLineF):
    def __eq__(self, other):
        x1 = self.x1() == other.x1()
        x2 = self.x2() == other.x2()
        y1 = self.y1() == other.y1()
        y2 = self.y2() == other.y2()
        return x1 and x2 and y1 and y2

    def __str__(self):
        return f"{self.x1()} {self.y1()} {self.x2()} {self.y2()}\n"


