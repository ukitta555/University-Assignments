import logging

from src.utils.graphical_types import QtSegment, DrawingBoardScene

logger = logging.getLogger(__name__)


class SegmentDrawingMachine:
    def __init__(self, drawing_board: DrawingBoardScene):
        self.drawing_board = drawing_board

    def draw_segments(self, segments):
        for raw_segment in segments:
            self._draw_segment(QtSegment(*raw_segment))

    def _draw_segment(self, new_segment):
        self.drawing_board.addSegment(new_segment)
        logger.info(f'Drew segment {new_segment}')

