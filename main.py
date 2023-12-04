# This is a sample Python script.
from ColorShape import ColorShape
import numpy as np
import cv2
import random


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    cs1 = ColorShape()
    print(cs1)
    print(hash(cs1))

    buffer = np.ones((400,400,3),dtype=float) * 0.75

    for i in range(50):
        cs_temp = ColorShape()
        cs_temp.draw_self_at(buffer, random.randint(20,380), random.randint(20,380))

    cv2.imshow("test",buffer)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
