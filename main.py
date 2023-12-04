from OpenAddressingSetFile import OpenAddressingSet
from ChainedSetFile import ChainedSet
from ColorShape import ColorShape, SHAPE_TYPE_EMPTY_BUT_SCANNABLE, SHAPE_TYPE_BALL, SHAPE_TYPE_DIAMOND, SHAPE_TYPE_BOX
import numpy as np
import cv2
import random

oaSet = OpenAddressingSet()
cSet = ChainedSet()

def demo_drawing():

    cs1 = ColorShape()
    print(cs1)
    print(hash(cs1))

    drawing_area = np.ones((400,400,3),dtype=float) * 0.75

    for i in range(50):
        cs_temp = ColorShape()
        cs_temp.draw_self_at(drawing_area, random.randint(20,380), random.randint(20,380))

    deadShape = ColorShape((0.5, 0.75, 1.0), "Z",SHAPE_TYPE_EMPTY_BUT_SCANNABLE)
    deadShape.draw_self_at(drawing_area, 200,200)

    cv2.imshow("test",drawing_area)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def draw_sets() -> None:
    """
    displays a window with our two sets in it, one above the other, and waits for the user to type a key.
    :return: None
    """
    global sets_drawing_area
    sets_drawing_area= np.ones((800,800,3), dtype=float) * 0.75
    oaSet.draw_hash_table(sets_drawing_area, (20, 20))
    cSet.draw_hash_table(sets_drawing_area, (20, 420))

    cv2.imshow("sets", sets_drawing_area)
    cv2.waitKey(0)


if __name__ == '__main__':
    demo_drawing()
    draw_sets()
