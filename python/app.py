from python.ui import Matching_ui as UI
from PyQt5.QtWidgets import QApplication, QSplashScreen, QFileDialog, QMessageBox
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

def show_info(parent, title="提示", message="操作成功"):
    msg_box = QMessageBox(parent)
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.exec_()

class matching_app:
    working_directory = None
    left_img_path = None
    right_img_path = None

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.ui = UI()
        self.ui.show()
        self.ui.directory_button.clicked.connect(self.set_directory)
        self.ui.left_btn.clicked.connect(self.get_left_image)
        self.ui.right_btn.clicked.connect(self.get_right_image)

    def set_directory(self):
        folder = QFileDialog.getExistingDirectory(self.ui, "选择工作空间")
        if folder:
            self.working_directory = folder
            self.ui.directory_label.setText(folder)

    def get_left_image(self):
        if not self.working_directory:
            show_info(self.ui, title = "提示", message= "请先选择工作空间！")
            return
        self.left_img_path, _ = QFileDialog.getOpenFileName(
                                                            self.ui,
                                                            "选择左影像",
                                                            self.working_directory,
                                                            "Images (*.png *.jpg *.jpeg *.bmp *.tif *.tiff)"
                                                        )
        if not self.left_img_path:
            return
        self.ui.left_img.set_image(self.left_img_path)

    def get_right_image(self):
        if not self.working_directory:
            show_info(self.ui, title = "提示", message= "请先选择工作空间！")
            return
        self.right_img_path, _ = QFileDialog.getOpenFileName(
                                                            self.ui,
                                                            "选择右影像",
                                                            self.working_directory,
                                                            "Images (*.png *.jpg *.jpeg *.bmp *.tif *.tiff)"
                                                        )
        if not self.right_img_path:
            return
        self.ui.right_img.set_image(self.right_img_path)
    
    def run(self):
        sys.exit(self.app.exec_())