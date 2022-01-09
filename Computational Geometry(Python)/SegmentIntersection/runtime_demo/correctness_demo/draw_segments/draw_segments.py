import logging

from runtime_demo.utils.type_aliases import DrawingBoardScene

logger = logging.getLogger(__name__)


class SegmentDrawingMachine:
    def __init__(self, drawing_board: DrawingBoardScene):
        self.drawing_board = drawing_board

    def draw_segments(self, segments):
        for segment in segments:
            self._draw_segment_(segment)

    def _draw_segment_(self, new_segment):
        self.drawing_board.addSegment(new_segment)
        logger.info(f'Drew segment {new_segment}')

