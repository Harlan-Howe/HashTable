from typing import Tuple
from AbstractSetFile import BasicAbstractSet, AdvancedAbstractSet
import numpy as np

class OpenAddressingSet(BasicAbstractSet):

    def __init__(self):
        pass

    def draw_hash_table(self, drawing_area: np.ndarray, start_pos: Tuple[int, int]) -> None:
        """
        draws all the ColorShapes in this set on the drawing_area in a way that illustrates how the hash table is
        organized.
        :param drawing_area: the surface on which to draw.
        :param start_pos: the upper-left corner of this hash table's drawing.
        :return:  None
        """
        pass
        # Hint: look at main's demo_drawing() for inspiration....
