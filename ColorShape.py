from typing import Tuple
import random
import numpy as np
import cv2

SHAPE_TYPE_BOX = 0
SHAPE_TYPE_BALL = 1
SHAPE_TYPE_DIAMOND = 2

SIZE = 16
class ColorShape:




    def __init__(self, color:Tuple[float] = None, letter: str = None, shape_type: int = -1):
        if color is None:
            color = (random.randint(96, 256)/256,
                     random.randint(96, 256)/256,
                     random.randint(96, 256)/256)
        self.__color__ = color

        if letter is None:
            letter = chr(random.randint(65,90))
        self.__letter__ = letter

        if shape_type == -1:
            shape_type = random.randint(0,2)
        self.__shape_type__ = shape_type

    def __repr__(self):
        return f"{self.__color__}\t{self.__letter__}\t{self.__shape_type__}"

    def draw_self_at(self, buffer:np.ndarray, x:int, y:int):
        if self.__shape_type__ == SHAPE_TYPE_BOX:
            cv2.rectangle(buffer,(x, y),(x+SIZE, y+SIZE),self.__color__,-1 )
        if self.__shape_type__ == SHAPE_TYPE_BALL:
            cv2.circle(buffer,center=(int(x+SIZE/2), int(y+SIZE/2)),radius= int(SIZE/2), color = self.__color__, thickness=-1)
        if self.__shape_type__ == SHAPE_TYPE_DIAMOND:
            pts = np.array([[int(x + SIZE/2), y],
                   [int(x + SIZE), int(y + SIZE/2)],
                   [int(x + SIZE/2), int(y + SIZE)],
                   [x , int(y + SIZE/2)]], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.fillPoly(buffer,[pts] ,self.__color__)
        cv2.putText(buffer, self.__letter__,  (int(x+SIZE/4),int(y+SIZE*3/4)), cv2.FONT_HERSHEY_SIMPLEX, 0.33, (0.25,0.25,0.25))




