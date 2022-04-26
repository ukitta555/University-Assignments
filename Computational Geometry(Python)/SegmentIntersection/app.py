from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QPen, QTransform
from PyQt5.QtWidgets import QSplitter

import design
from src.correctness_demo.correctness_demo import run_correctness_test_fast, run_correctness_test_slow
from src.performance_demo.performance_demo import run_performance_test_slow, \
    run_performance_test_fast
from src.utils.graphical_types import DrawingBoardScene


class App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self._init_canvas()
        self._init_pens()
        self._init_brushes()
        self._connect_buttons()

    def _init_canvas(self):
        self.DrawingBoardScene: DrawingBoardScene = DrawingBoardScene()
        matrix = QTransform(1, 0, 0, 0, -1, 0, 0, 0, 1)
        self.DrawingBoard.setTransform(matrix)
        self.DrawingBoard.setScene(self.DrawingBoardScene)


    def _init_pens(self):
        self.RedPen = QPen(Qt.red)
        self.GreenPen = QPen(Qt.green)

    def _init_brushes(self):
        self.Brush = QBrush(Qt.green)

    def _connect_buttons(self):
        self.CorrectnessTestButton_Slow.clicked.connect(
            lambda: run_correctness_test_slow(
                        self.DrawingBoard,
                        self.DrawingBoardScene
                    )
        )
        self.CorrectnessTestButton_Fast.clicked.connect(
            lambda: run_correctness_test_fast(
                        self.DrawingBoard,
                        self.DrawingBoardScene
                    )
        )
        self.PerformanceTestButton_Slow.clicked.connect(
            lambda: run_performance_test_slow(
                        self.DrawingBoard,
                        self.DrawingBoardScene
                    )
        )
        self.PerformanceTestButton_Fast.clicked.connect(
            lambda: run_performance_test_fast(
                        self.DrawingBoard,
                        self.DrawingBoardScene
                    )
        )