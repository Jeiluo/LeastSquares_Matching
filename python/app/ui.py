from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout, QDesktopWidget, QHBoxLayout, QSizePolicy, QLineEdit, QGridLayout
from PyQt5.QtCore import Qt
from python.app.ImageLabel import ClickableImageLabel, Window_Label

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
        main_layout = QHBoxLayout()
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

        self.choosing_widget = QWidget()
        self.choosing_widget.setObjectName("choosing_widget")
        self.choosing_widget.setStyleSheet(
                    """
        QWidget#choosing_widget {
            border: 1px solid gray;
            border-radius: 4px;
            padding: 4px;
            background-color: #f9f9f9;
        }
        """
        )
        choosing_layout = QVBoxLayout()
        choosing_layout.setContentsMargins(2, 2, 2, 2)
        choosing_layout.setSpacing(4)
        self.choosing_widget.setLayout(choosing_layout)

        self.matching_widget = QWidget()
        self.matching_widget.setObjectName("choosing_widget")
        self.matching_widget.setStyleSheet(
                    """
        QWidget#choosing_widget {
            border: 1px solid gray;
            border-radius: 4px;
            padding: 4px;
            background-color: #f9f9f9;
        }
        """
        )
        matching_layout = QVBoxLayout()
        matching_layout.setContentsMargins(2, 2, 2, 2)
        matching_layout.setSpacing(4)
        self.matching_widget.setLayout(matching_layout)

        self.choosing_label = QLabel("手动选取同名点")
        choosing_layout.addWidget(self.choosing_label, alignment = Qt.AlignHCenter)

        self.matching_label = QLabel("自动匹配同名点")
        matching_layout.addWidget(self.matching_label, alignment = Qt.AlignHCenter)

        row_layout = QHBoxLayout()
        row_layout.setContentsMargins(0, 0, 0, 0)
        row_layout.setSpacing(4)
        self.windowsize_label = QLabel("平差窗口大小:")
        self.windowsize_line_edit = QLineEdit()

        row_layout.addWidget(self.windowsize_label)
        row_layout.addWidget(self.windowsize_line_edit, 1)
        choosing_layout.addLayout(row_layout)

        self.choose_btn = QPushButton("平差计算")
        choosing_layout.addWidget(self.choose_btn, alignment= Qt.AlignHCenter)

        row_layout = QHBoxLayout()
        row_layout.setContentsMargins(0, 0, 0, 0)
        row_layout.setSpacing(4)
        self.windowsize_label2 = QLabel("匹配算子窗口大小:")
        self.windowsize_line_edit2 = QLineEdit()

        row_layout.addWidget(self.windowsize_label2)
        row_layout.addWidget(self.windowsize_line_edit2, 1)
        matching_layout.addLayout(row_layout)
        
        wrapper = QWidget()
        wrapper_layout = QVBoxLayout()
        wrapper.setLayout(wrapper_layout)
        wrapper_layout.setContentsMargins(0, 0, 0, 0)
        wrapper_layout.setSpacing(0)

        wrapper_layout.addWidget(self.directory_widget, alignment=Qt.AlignLeft)
        wrapper_layout.addWidget(self.img_widget, alignment=Qt.AlignHCenter)
        wrapper_layout.addWidget(self.choosing_widget, alignment=Qt.AlignHCenter)
        wrapper_layout.addWidget(self.matching_widget, alignment = Qt.AlignHCenter)

        self.result_widget = QWidget(self)
        self.result_widget.setStyleSheet("border: 3px solid red;")
        self.result_widget.raise_()
        result_layout = QGridLayout()
        self.result_widget.setLayout(result_layout)
        self.result_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.left_window_origin_label = QLabel("左窗口原图")
        self.left_window_origin = Window_Label()
        self.right_window_origin_label = QLabel("右窗口原图")
        self.right_window_origin = Window_Label()
        self.left_window_label = QLabel("左窗口原图")
        self.left_window = Window_Label()
        self.right_window_label = QLabel("右窗口纠正图")
        self.right_window = Window_Label()

        result_layout.addWidget(self.left_window_origin_label, 0, 0)
        result_layout.addWidget(self.left_window_origin, 1, 0)
        result_layout.addWidget(self.right_window_origin_label, 0, 1)
        result_layout.addWidget(self.right_window_origin, 1, 1)

        result_layout.addWidget(self.left_window_label, 2, 0)
        result_layout.addWidget(self.left_window, 3, 0)
        result_layout.addWidget(self.right_window_label, 2, 1)
        result_layout.addWidget(self.right_window, 3, 1)

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

        self.choosing_widget.setFixedWidth(int(self.width() * 0.2))
        self.choosing_label.setFixedHeight(int(self.height() * 0.02)+1)
        self.choosing_label.setStyleSheet(f"font-size:{int(self.height() * 0.02)}px;")
        self.windowsize_label.setFixedHeight(int(self.height() * 0.02)+1)
        self.windowsize_label.setStyleSheet(f"font-size:{int(self.height() * 0.02)}px;")
        self.windowsize_line_edit.setFixedHeight(int(self.height() * 0.02)+1)
        self.windowsize_line_edit.setStyleSheet(f"font-size:{int(self.height() * 0.02)}px;")
        self.choose_btn.setFixedSize(int(self.width() * 0.1), int(self.height() * 0.03))
        self.choose_btn.setStyleSheet(f"font-size:{int(self.height() * 0.015)}px;")

        self.matching_widget.setFixedWidth(int(self.width() * 0.2))
        self.matching_label.setFixedHeight(int(self.height() * 0.02)+1)
        self.matching_label.setStyleSheet(f"font-size:{int(self.height() * 0.02)}px;")
        self.windowsize_label2.setFixedHeight(int(self.height() * 0.02)+1)
        self.windowsize_label2.setStyleSheet(f"font-size:{int(self.height() * 0.02)}px;")
        self.windowsize_line_edit2.setFixedHeight(int(self.height() * 0.02)+1)
        self.windowsize_line_edit2.setStyleSheet(f"font-size:{int(self.height() * 0.02)}px;")

        self.result_widget.move(int(self.width()*0.65), int(self.height()*0.65))
        self.result_widget.setFixedSize(int(self.width()*0.18), int(self.height()*0.32))
        self.left_window_origin.setFixedSize(int(self.width()*0.06), int(self.width()*0.06))
        self.right_window_origin.setFixedSize(int(self.width()*0.06), int(self.width()*0.06))
        self.left_window.setFixedSize(int(self.width()*0.06), int(self.width()*0.06))
        self.right_window.setFixedSize(int(self.width()*0.06), int(self.width()*0.06))

    def update_label_font(self):
        for label in [self.left_img, self.right_img]:
            h = label.height()
            font_size = max(8, int(h * 0.10))
            label.setStyleSheet(
                f"border:1px solid gray; font-family:Consolas; font-size:{font_size}px;"
            )
