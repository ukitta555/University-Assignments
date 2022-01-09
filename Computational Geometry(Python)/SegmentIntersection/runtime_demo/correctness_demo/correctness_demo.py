from runtime_demo.correctness_demo.draw_segments.draw_segments import SegmentDrawingMachine
from runtime_demo.correctness_demo.read_segments.read_segments_from_file import read_segments_from_file
from runtime_demo.correctness_demo.utils.utils import convert_to_scientific
from runtime_demo.utils.type_aliases import DrawingBoardScene, Segment


def run_correctness_test_slow(drawing_board: DrawingBoardScene):
    raw_segments = read_segments_from_file()


    SegmentDrawingMachine(drawing_board).draw_segments(raw_segments)
    segments: list[Segment] = convert_to_scientific(raw_segments)

    print(segments[0].intersection(segments[1]))