import typing

from PyQt5 import QtGui, QtCore, Qt
from PyQt5.QtCore import QLineF
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsLineItem


class DrawingBoardScene(QGraphicsScene):
    def addSegment(self, line: QtCore.QLineF, pen: typing.Union[QtGui.QPen, QtGui.QColor, QtCore.Qt.GlobalColor,
                                                                QtGui.QGradient] = QtGui.QPen(Qt.Qt.black)) -> \
            QGraphicsLineItem:
        return super().addLine(line, pen)


class Segment(QLineF):
    def __str__(self):
        return f"({self.x1()} {self.y1()} {self.x2()} {self.y2()})"


class SegmentForMockFile(Segment):
    def __str__(self):
        return f"{self.x1()} {self.y1()} {self.x2()} {self.y2()}\n"


RawSegment: typing.TypeAlias = tuple[float, float, float, float]