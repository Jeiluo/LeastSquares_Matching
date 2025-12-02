from ._lsmatching import Matching as LSMatching
import numpy as np

class Matching:
    def __init__(self, left_image_path: str, right_image_path: str):
        self.matching = LSMatching(left_image_path, right_image_path)
    
    def set_params(self, windowsize: int):
        self.matching.set_params(int(windowsize))

    def set_centers(self, x1: int, y1: int, x2: int, y2: int):
        self.matching.set_centers(int(x1), int(y1), int(x2), int(y2))

    def calculate(self):
        self.matching.calculate()

    def get_left_window(self) -> np.ndarray:
        return self._matching.get_left_window()