from runtime_demo.correctness_demo.draw_segments.draw_segments import SegmentDrawingMachine
from runtime_demo.correctness_demo.read_segments.read_segments_from_file import read_segments_from_file
from runtime_demo.utils.type_aliases import DrawingBoardScene


def run_correctness_test(drawing_board: DrawingBoardScene):
    segments = read_segments_from_file()
    SegmentDrawingMachine(drawing_board).draw_segments(segments)


