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

        self.init_canvas()
        self.init_pens()
        self.init_brushes()
        self.connect_buttons()

        self.DrawingBoardScene.addLine(QLineF(0, 0, 634, 571), self.RedPen)
        self.DrawingBoardScene.addLine(QLineF(100, 100, 200, 200), self.GreenPen)


    def init_canvas(self):
        self.DrawingBoardScene: DrawingBoardScene = DrawingBoardScene()
        self.DrawingBoard.setScene(self.DrawingBoardScene)

    def init_pens(self):
        self.RedPen = QPen(Qt.red)
        self.GreenPen = QPen(Qt.green)

    def init_brushes(self):
        self.Brush = QBrush(Qt.green)

    def connect_buttons(self):
        self.CorrectnessTestButton.clicked.connect(lambda: run_correctness_test(self.DrawingBoardScene))
        self.PerformanceTestButton.clicked.connect(lambda: run_performance_test(self.DrawingBoardScene))
