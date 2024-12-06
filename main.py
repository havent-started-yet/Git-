import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QPainter, QColor


class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.circles = []

    def add_circle(self, x, y, radius, color):
        self.circles.append((x, y, radius, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        for (x, y, radius, color) in self.circles:
            painter.setBrush(color)
            painter.drawEllipse(x, y, radius, radius)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Random Circle Drawer")
        self.setGeometry(100, 100, 800, 600)

        self.circle_widget = CircleWidget()

        self.button = QPushButton("Draw Circle")
        self.button.clicked.connect(self.draw_circle)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.circle_widget)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def draw_circle(self):
        x = random.randint(0, self.circle_widget.width())
        y = random.randint(0, self.circle_widget.height())
        radius = random.randint(10, 200)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.circle_widget.add_circle(x, y, radius, color)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())
