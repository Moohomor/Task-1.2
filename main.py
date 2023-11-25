import sys

from random import randint as ri
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btn.clicked.connect(self.run)
        self.pain = False

    def run(self):
        self.pain = True
        self.update()

    def paintEvent(self, e):
        if self.pain:
            g = self.frameGeometry()
            qp = QPainter()
            qp.begin(self)
            x, y, d = ri(10,g.width()), ri(10,g.height()), ri(10,100)
            qp.setBrush(QColor(255, 255, 0))
            qp.drawEllipse(x, y, d, d)
            x, y, d = ri(10,100), ri(10,100), ri(10,100)
            qp.setBrush(QColor(255, 255, 0))
            qp.drawEllipse(x, y, d, d)
            x, y, d = ri(10,100), ri(10,100), ri(10,100)
            qp.setBrush(QColor(255, 255, 0))
            qp.drawEllipse(x, y, d, d)
            qp.end()
        self.pain = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
