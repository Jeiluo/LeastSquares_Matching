from python.ui import Matching_ui as UI
from PyQt5.QtWidgets import QApplication, QSplashScreen
import sys

class matching_app:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.ui = UI()
        self.ui.show()
    
    def run(self):
        sys.exit(self.app.exec_())