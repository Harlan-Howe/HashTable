from typing import Tuple, Optional
import random
import numpy as np
import cv2

SHAPE_TYPE_BOX = 0
SHAPE_TYPE_BALL = 1
SHAPE_TYPE_DIAMOND = 2
SHAPE_TYPE_EMPTY_BUT_SCANNABLE = -1 # what we put into the hash table (if it uses open addressing) when we delete an item.

SIZE = 16
class ColorShape:




    def __init__(self, color:Optional[Tuple[float, float, float]] = None, letter: str = None, shape_type: int = -2):
        if color is None:
            color = (random.randint(96, 256)/256,
                     random.randint(96, 256)/256,
                     random.randint(96, 256)/256)
        self.__color__ = color

        if letter is None:
            letter = chr(random.randint(65,90))
        self.__letter__ = letter

        if shape_type == -2:
            shape_type = random.randint(0,2)
        self.__shape_type__ = shape_type

    def __repr__(self):
        return f"{self.__color__}\t{self.__letter__}\t{self.__shape_type__}"

    def draw_self_at(self, drawing_area: np.ndarray, x:int, y:int):
        if self.__shape_type__ == SHAPE_TYPE_BOX:
            cv2.rectangle(drawing_area, (x, y), (x + SIZE, y + SIZE), self.__color__, -1)
        if self.__shape_type__ == SHAPE_TYPE_BALL:
            cv2.circle(drawing_area, center=(int(x + SIZE / 2), int(y + SIZE / 2)), radius= int(SIZE / 2), color = self.__color__, thickness=-1)
        if self.__shape_type__ == SHAPE_TYPE_DIAMOND:
            pts = np.array([[int(x + SIZE/2), y],
                   [int(x + SIZE), int(y + SIZE/2)],
                   [int(x + SIZE/2), int(y + SIZE)],
                   [x , int(y + SIZE/2)]], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.fillPoly(drawing_area, [pts], self.__color__)
        if self.__shape_type__ == SHAPE_TYPE_EMPTY_BUT_SCANNABLE:
            cv2.rectangle(drawing_area, (x, y), (x + SIZE, y + SIZE), (0, 0, 0), 1)
            cv2.line(drawing_area, (x, y), (x + SIZE, y + SIZE), (0, 0, 0), 1)
            cv2.line(drawing_area, (x + SIZE, y), (x, y + SIZE), (0, 0, 0), 1)
            return  # don't draw the letter if it is an empty spot.

        cv2.putText(drawing_area, self.__letter__, (int(x + SIZE / 4), int(y + SIZE * 3 / 4)), cv2.FONT_HERSHEY_SIMPLEX, 0.33, (0.25, 0.25, 0.25))

    def __eq__(self, __value) -> bool:
        """
        lets the "==" operator work for ColorShapes.
        :param __value: another ColorShape to compare
        :return: whether the content of this shape and the __value ColorShape match perfectly.
        """
        if not isinstance(__value, ColorShape):
            return False
        if self.__shape_type__ != __value.__shape_type__:
            return False
        if self.__letter__ != __value.__letter__:
            return False
        if self.__color__ != __value.__color__:
            return False
        return True

    def __hash__(self) -> int:
        """
        lets the "hash()" method work on ColorShapes....
        :return: a hash code for this ColorShape object.
        """
        return hash(self.__letter__) + hash(self.__color__) + hash(self.__shape_type__)

    @classmethod
    def deleted_spot(cls):
        """
        a 'factory" method that will create one of the empty-but-scannable ColorShapes. Invoke by
        something like
        blankspot = ColorShape.deleted_spot()
        :return:  a new ColorShape object with the shapetype of SHAPE_TYPE_EMPTY_BUT_SCANNABLE
        """
        return ColorShape(shape_type=SHAPE_TYPE_EMPTY_BUT_SCANNABLE)

    def is_real(self) -> bool:
        """
        convenience method for determining whether a ColorShape is one of the box, circle or trianlge type, rather
        than the placeholder (empty-but-scannable) type.
        :return: whether this is an actual, shape of type square, circle, diamond.
        """
        return self.__shape_type__ != SHAPE_TYPE_EMPTY_BUT_SCANNABLE


