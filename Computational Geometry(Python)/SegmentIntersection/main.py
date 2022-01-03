import logging
import sys
from PyQt5 import QtWidgets
import design
from app import App


def main():
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
