from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QPainter, QPen
from PyQt5.QtCore import Qt, QPoint

class ClickableImageLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pixmap_orig = None # 原图像
        self.click_point = None # 点击坐标（像素坐标）
        self.setAlignment(Qt.AlignCenter)

    def set_image(self, image_path):
        pixmap = QPixmap(image_path)
        self.pixmap_orig = pixmap
        self.click_point = None
        self.update_display()

    def update_display(self):
        if self.pixmap_orig is None:
            return
        # 按 QLabel 尺寸缩放图像，保持纵横比
        scaled_pix = self.pixmap_orig.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        pix = QPixmap(scaled_pix)
        painter = QPainter(pix)
        pen = QPen(Qt.red)
        pen.setWidth(3)
        painter.setPen(pen)
        # 如果有点击点，绘制红点
        if self.click_point is not None:
            x, y = self.click_point
            px = x * scaled_pix.width() / self.pixmap_orig.width()
            py = y * scaled_pix.height() / self.pixmap_orig.height()
            
            # 绘制红色圆圈
            pen = QPen(Qt.red)
            pen.setWidth(1)
            painter.setPen(pen)
            radius = 7  # 圆半径，可调
            painter.drawEllipse(int(px - radius), int(py - radius), 2*radius, 2*radius)

            # 绘制红色填充点在中心
            painter.setBrush(Qt.red)
            painter.drawEllipse(int(px - 1), int(py - 1), 2, 2)  # 小圆点中心
        painter.end()
        self.setPixmap(pix)

    def mousePressEvent(self, event):
        if self.pixmap_orig is None:
            return
        click_pos = event.pos()
        scaled_pix = self.pixmap().size()
        label_width, label_height = self.width(), self.height()
        offset_x = (label_width - scaled_pix.width()) / 2
        offset_y = (label_height - scaled_pix.height()) / 2
        x_in_pix = click_pos.x() - offset_x
        y_in_pix = click_pos.y() - offset_y
        if 0 <= x_in_pix <= scaled_pix.width() and 0 <= y_in_pix <= scaled_pix.height():
            # 转换为原图像像素坐标
            x_img = x_in_pix * self.pixmap_orig.width() / scaled_pix.width()
            y_img = y_in_pix * self.pixmap_orig.height() / scaled_pix.height()
            self.click_point = (x_img, y_img) # 每次点击覆盖
            print(f"点击位置（图像像素坐标）：({int(x_img)}, {int(y_img)})")
            self.update_display()