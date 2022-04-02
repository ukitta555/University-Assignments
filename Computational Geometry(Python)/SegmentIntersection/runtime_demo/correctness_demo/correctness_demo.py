from runtime_demo.correctness_demo.draw_segments.draw_segments import SegmentDrawingMachine
from runtime_demo.correctness_demo.read_segments.read_segments_from_file import ReadSegments
from runtime_demo.correctness_demo.utils.utils import convert_to_scientific
from runtime_demo.utils.type_aliases import DrawingBoardScene, MySegment


def run_correctness_test_slow(drawing_board: DrawingBoardScene):
    raw_segments = ReadSegments().run(filename="small_example.txt")

    SegmentDrawingMachine(drawing_board).draw_segments(raw_segments)
    segments: list[MySegment] = convert_to_scientific(raw_segments)

    print(segments[0].intersection(segments[1]))