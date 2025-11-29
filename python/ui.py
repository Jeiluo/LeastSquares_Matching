from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout, QDesktopWidget

class Matching_ui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Least-Square Matching Application")
        self.resize(800, 600)  # 设置大小
        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())