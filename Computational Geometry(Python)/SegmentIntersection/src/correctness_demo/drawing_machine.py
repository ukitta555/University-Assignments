import logging

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QBrush

from src.utils.computational_types import MyPoint, MySegment
from src.utils.graphical_types import QtSegment, DrawingBoardScene

logger = logging.getLogger(__name__)


class DrawingMachine:
    def __init__(self, drawing_board: DrawingBoardScene):
        self.drawing_board = drawing_board



    def draw_segments(self, segments):
        for segment in segments:
            if type(segment) is tuple:
                self._draw_segment(QtSegment(*segment))
            elif type(segment) is MySegment:
                self._draw_segment(QtSegment(segment.start.x, segment.start.y, segment.end.x, segment.end.y))

    def draw_intersections(self, intersections: set[MyPoint]):
        for intersection in intersections:
            self._draw_point(intersection)

    def _draw_point(self, point: MyPoint):
        self.drawing_board.addEllipse(point.x-5, point.y-5, 10, 10, brush=QBrush(Qt.red, Qt.SolidPattern))
        logger.info(f'Drew intersection {point}')

    def _draw_segment(self, new_segment):
        # self.drawing_board.addSegment(new_segment, pen=QPen(Qt.black, 15))
        self.drawing_board.addSegment(new_segment)
        logger.info(f'Drew segment {new_segment}')

