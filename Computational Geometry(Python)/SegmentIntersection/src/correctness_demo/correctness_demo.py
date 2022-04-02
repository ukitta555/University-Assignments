from src.correctness_demo.segment_drawing_machine import SegmentDrawingMachine
from src.correctness_demo.read_segments.segment_reader import SegmentReader
from src.correctness_demo.utils.utils import convert_to_scientific
from src.utils.computational_types import MySegment
from src.utils.graphical_types import DrawingBoardScene


def run_correctness_test_slow(drawing_board: DrawingBoardScene):
    raw_segments = SegmentReader().run(filename="small_example.txt")
    SegmentDrawingMachine(drawing_board).draw_segments(raw_segments)
    segments: list[MySegment] = convert_to_scientific(raw_segments)

    print(segments[0].intersection(segments[1]))