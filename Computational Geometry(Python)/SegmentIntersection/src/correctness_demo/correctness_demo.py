from PyQt5.QtCore import Qt

from src.algorithms.brute_force.brute_force_solution import find_intersections_slow
from src.algorithms.sweep_line.sweep_line import find_intersections_fast
from src.correctness_demo.drawing_machine import DrawingMachine
from src.correctness_demo.read_segments.segment_reader import SegmentReader
from src.correctness_demo.utils.utils import convert_to_scientific
from src.utils.computational_types import MySegment
from src.utils.graphical_types import DrawingBoardScene


def run_correctness_test_slow(drawing_board, drawing_board_scene: DrawingBoardScene):
    raw_segments = SegmentReader().run(filename="small_example.txt")
    drawing_board_scene.clear()
    drawing_board_scene.setSceneRect(0, 0, 1000, 1000)
    drawing_board.fitInView(drawing_board_scene.sceneRect(), Qt.KeepAspectRatio)
    drawing_machine = DrawingMachine(drawing_board_scene)
    drawing_machine.draw_segments(raw_segments)

    segments: list[MySegment] = convert_to_scientific(raw_segments)
    intersections = find_intersections_slow(segments)

    drawing_machine.draw_intersections(intersections=intersections)


def run_correctness_test_fast(drawing_board, drawing_board_scene: DrawingBoardScene):
    from src.algorithms.sweep_line.sweep_line import SweepLine
    raw_segments = SegmentReader().run(filename="small_example.txt")
    segments: list[MySegment] = convert_to_scientific(raw_segments)

    segments = SweepLine.random_rotation_if_horizontal_lines_are_present(segments)
    intersections = find_intersections_fast(segments)

    drawing_board_scene.clear()
    drawing_board_scene.setSceneRect(0, 0, 1000, 1000)
    drawing_board.fitInView(drawing_board_scene.sceneRect(), Qt.KeepAspectRatio)

    drawing_machine = DrawingMachine(drawing_board_scene)
    drawing_machine.draw_segments(segments)
    drawing_machine.draw_intersections(intersections=intersections)