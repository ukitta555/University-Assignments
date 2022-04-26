import random

from PyQt5.QtCore import Qt

from src.algorithms.brute_force.brute_force_solution import find_intersections_slow
from src.algorithms.sweep_line.sweep_line import find_intersections_fast
from src.correctness_demo.drawing_machine import DrawingMachine
from src.correctness_demo.read_segments.segment_reader import SegmentReader
from src.correctness_demo.utils.utils import convert_to_scientific
from src.utils.computational_types import MySegment
from src.utils.graphical_types import DrawingBoardScene



def generate_file():
    outfile = open('big_example.txt', 'w')
    for i in range(10000):
        x = random.randint(500, 2000)
        y = random.randint(500, 2000)
        w = random.randint(500, 2000)
        z = random.randint(500, 2000)
        outfile.write("{} {} {} {}\n".format(x, y, w, z))
    outfile.close()

def generate_file_no_intersections():
    outfile = open('big_example.txt', 'w')

    x_s = list(range(500, 1000, 10))
    y_s = 10

    while y_s < 50:
        for x in x_s:
            outfile.write("{} {} {} {}\n".format(x, y_s, x, y_s + 20))
        y_s += 30

    outfile.close()


def run_performance_test_slow(drawing_board, drawing_board_scene: DrawingBoardScene):
    # generate_file()

    raw_segments = SegmentReader().run(filename="big_example.txt")
    segments: list[MySegment] = convert_to_scientific(raw_segments)
    intersections = find_intersections_slow(segments)

    drawing_board_scene.clear()
    drawing_board_scene.setSceneRect(0, 0, 2000, 200)
    drawing_board.fitInView(drawing_board_scene.sceneRect(), Qt.IgnoreAspectRatio)
    drawing_machine = DrawingMachine(drawing_board_scene)
    drawing_machine.draw_segments(raw_segments)
    drawing_machine.draw_intersections(intersections=intersections)

def run_performance_test_fast(drawing_board, drawing_board_scene: DrawingBoardScene):
    from src.algorithms.sweep_line.sweep_line import SweepLine

    # generate_file_no_intersections()

    raw_segments = SegmentReader().run(filename="big_example.txt")
    segments: list[MySegment] = convert_to_scientific(raw_segments)
    segments = SweepLine.random_rotation_if_horizontal_lines_are_present(segments)

    intersections = find_intersections_fast(segments)

    drawing_board_scene.clear()
    drawing_board_scene.setSceneRect(0, 0, 1000, 1000)
    drawing_board.fitInView(drawing_board_scene.sceneRect(), Qt.IgnoreAspectRatio)

    drawing_machine = DrawingMachine(drawing_board_scene)
    drawing_machine.draw_segments(segments)
    drawing_machine.draw_intersections(intersections=intersections)