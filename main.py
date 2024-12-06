import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6 import uic


class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.circles = []

    def add_circle(self, x, y, radius):
        self.circles.append((x, y, radius))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        for (x, y, radius) in self.circles:
            painter.setBrush(QColor('yellow'))
            painter.drawEllipse(x, y, radius, radius)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.circle_widget = CircleWidget()
        self.button.clicked.connect(self.draw_circle)

        self.layout.addWidget(self.circle_widget)

        self.container.setLayout(self.layout)

    def draw_circle(self):
        x = random.randint(0, self.circle_widget.width())
        y = random.randint(0, self.circle_widget.height())
        radius = random.randint(10, 200)

        self.circle_widget.add_circle(x, y, radius)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
