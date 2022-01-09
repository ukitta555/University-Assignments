import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QLineF
from PyQt5.QtGui import QBrush, QPen

import design
from runtime_demo.correctness_demo.correctness_demo import run_correctness_test
from runtime_demo.performance_demo.performance_demo import run_performance_test
from runtime_demo.utils.type_aliases import DrawingBoardScene


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
        self.DrawingBoard.setScene(self.DrawingBoardScene)

    def _init_pens(self):
        self.RedPen = QPen(Qt.red)
        self.GreenPen = QPen(Qt.green)

    def _init_brushes(self):
        self.Brush = QBrush(Qt.green)

    def _connect_buttons(self):
        self.CorrectnessTestButton_Slow.clicked.connect(lambda: run_correctness_test(self.DrawingBoardScene))
        self.PerformanceTestButton_Slow.clicked.connect(lambda: run_performance_test(self.DrawingBoardScene))
