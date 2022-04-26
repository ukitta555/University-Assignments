import logging
import sys

from PyQt5 import QtWidgets
from app import App


def main():
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
