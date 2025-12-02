from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout, QDesktopWidget, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt
from python.ImageLabel import ClickableImageLabel

class Matching_ui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Least-Square Matching Application")
        self.resize(800, 600)
        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        img_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        self.left_img = ClickableImageLabel("Left Image")
        self.left_img.setAlignment(Qt.AlignCenter)
        self.left_btn = QPushButton("选择左影像")
        left_layout.addWidget(self.left_img)
        left_layout.addWidget(self.left_btn, alignment=Qt.AlignHCenter)

        right_layout = QVBoxLayout()
        self.right_img = ClickableImageLabel("Right Image")
        self.right_img.setAlignment(Qt.AlignCenter)
        self.right_btn = QPushButton("选择右影像")
        right_layout.addWidget(self.right_img)
        right_layout.addWidget(self.right_btn, alignment=Qt.AlignHCenter)

        img_layout.addLayout(left_layout)
        img_layout.addLayout(right_layout)

        directory_layout = QHBoxLayout()
        self.directory_button = QPushButton("选择工作空间")
        self.directory_label = QLabel("当前工作空间未选择")
        self.directory_label.setStyleSheet("padding: 2px;")
        self.directory_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        directory_layout.addWidget(self.directory_button)
        directory_layout.addWidget(self.directory_label)
        directory_layout.setAlignment(Qt.AlignLeft)
        directory_layout.addStretch()

        self.directory_widget = QWidget()
        self.directory_widget.setLayout(directory_layout)
        
        self.img_widget = QWidget()
        self.img_widget.setLayout(img_layout)
        
        wrapper = QWidget()
        wrapper_layout = QVBoxLayout()
        wrapper.setLayout(wrapper_layout)
        wrapper_layout.setContentsMargins(0, 0, 0, 0)
        wrapper_layout.setSpacing(0)

        wrapper_layout.addWidget(self.directory_widget, alignment=Qt.AlignLeft)
        wrapper_layout.addWidget(self.img_widget, alignment=Qt.AlignHCenter)

        main_layout.addWidget(wrapper, alignment=Qt.AlignHCenter)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        h = int(self.height() * 0.35)
        w = int(h*7/4)
        self.left_img.setFixedSize(w, h)
        self.right_img.setFixedSize(w, h)
        self.directory_button.setFixedSize(int(self.height() * 0.05*4.0), int(self.height() * 0.05))
        self.directory_label.setFixedSize(int(self.height() * 0.05*20.0), int(self.height() * 0.05))
        self.update_label_font()
        self.directory_widget.setFixedHeight(int(self.height() * 0.05)+12)
        self.img_widget.setMaximumHeight(self.left_img.sizeHint().height()+self.left_btn.sizeHint().height()+int(self.height() * 0.1))
        self.left_btn.setFixedWidth(int(self.left_img.sizeHint().width()*0.5))
        self.right_btn.setFixedWidth(int(self.left_img.sizeHint().width()*0.5))
        self.left_btn.setFixedHeight(int(self.height() * 0.08))
        self.right_btn.setFixedHeight(int(self.height() * 0.08))

    def update_label_font(self):
        for label in [self.left_img, self.right_img]:
            h = label.height()
            font_size = max(8, int(h * 0.10))
            label.setStyleSheet(
                f"border:1px solid gray; font-family:Consolas; font-size:{font_size}px;"
            )
