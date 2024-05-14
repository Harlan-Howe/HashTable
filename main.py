from OpenAddressingSetFile import OpenAddressingSet
from ChainedSetFile import ChainedSet
from AbstractSetFile import AdvancedAbstractSet
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
    cv2.waitKey(1) # wait 1 millisecond for a keystroke before returning. Make this a zero if you want to wait
    #                  indefinitely for a keystroke.


def basic_testing():
    # this will be a list of items we think are in the sets.
    added_items = []

    # add 10 items to both sets, and keep them in another array for later reference.
    for i in range(1):  # update this to 10 when you're ready.
        shape = ColorShape()
        added_items.append(shape)
        oaSet.append(shape)
        cSet.append(shape)
    draw_sets()

    # here's a color shape that we might use outside of the sets.
    current_color_shape:ColorShape = ColorShape()

    while True:
        # display the shapes we think are in the sets
        for i in range(len(added_items)):
            print(f"{i}\t{added_items[i]}")

        # display the current color shape that is independent of the sets
        print(f"Current Color Shape: {current_color_shape}")

        # Menu and responses
        response = input("(A))dd, (R)emove, (F)ind, (G)enerate Random CCS, (P)ick CCS from list? ")
        response = response[0].lower()
        if response == "a":
            prompt = "How many to add? (or -1 to add current shape)"
            num_to_add = int(input(prompt))
            if num_to_add == -1:
                added_OA = oaSet.append(current_color_shape)
                added_chained = cSet.append(current_color_shape)
                print(f"\n{added_OA=}\t{added_chained=}")
                if added_OA and added_chained:
                    added_items.append(current_color_shape)
            else:
                for i in range(num_to_add):
                    shape = ColorShape()
                    added_items.append(shape)
                    oaSet.append(shape)
                    cSet.append(shape)
            print("click in the window and press a key to continue.")
            draw_sets()
        if response == "r":
            num = int(input("Which item in the list above? (or -1 for the currrent color shape" ))
            if num == -1:
                item_to_remove = current_color_shape

            elif num < 0 or num >= len(added_items):
                print("out of range.")
                continue
            item_to_remove = added_items[num]
            del(added_items[num])
            oaSet.remove(item_to_remove)
            cSet.remove(item_to_remove)
            print("click in the window and press a key to continue.")
            draw_sets()
        if response == "f":
            num = int(input("Which item in the list above, or -1 for the current color shape?"))
            if num == -1:
                item_to_find = current_color_shape
            else:
                if num < 0 or num >= len(added_items):
                    print("out of range.")
                    continue
                item_to_find = added_items[num]
            print(f"\nSearching for {item_to_find} --> OpenAddressing: {item_to_find in oaSet} "
                  f"| ChainAddressing: {item_to_find in cSet}")
        if response == "g":
            current_color_shape = ColorShape()
        if response == "p":
            num = int(input("which item in the list above should we copy into the current color shape? "))
            if num < 0 or num >=len(added_items):
                print("out of range.")
                continue
            current_color_shape = added_items[num]

def advanced_test_for_two_sets(set1:AdvancedAbstractSet, set2:AdvancedAbstractSet):
    for i in range(20):
        cs = ColorShape()
        if random.random() < 0.5:
            set1 += cs
        if random.random() < 0.5:
            set2 += cs

    print(f"Set 1: {simplified_set_list(set1.to_list())}")
    print(f"Set 2: {simplified_set_list(set2.to_list())}")

    print("-"*20)
    print(f"Set 1 - Set 2: {simplified_set_list((set1 - set2).to_list())}")
    print(f"Set 2 - Set 1: {simplified_set_list((set2 - set1).to_list())}")

    print("-"*20)
    print(f"Set1 and Set2: {simplified_set_list((set1 & set2).to_list())}" )
    print(f"Set1 or Set2: {simplified_set_list((set1 | set2).to_list())}")

    print("-"*20)

    print(f"(s1-s2) | (s1 & s2): {simplified_set_list(((set1-set2) | (set1 & set2)).to_list())}")
    print(f"s1:                  {simplified_set_list(set1.to_list())}")
    print("These should match....")

    print("-" * 20)
    print(f"Set1 subset of Set2: {set2.subset(set1)}")
    print(f"Set2 subset of Set1: {set1.subset(set2)}")
    print(f"(s1-s2) subset of Set1: {set1.subset(set1-set2)}")
    print(f"(s1-s2) subset of Set2: {set2.subset(set1 - set2)}")
    print(f"(s1 & s2) subset of Set1: {set1.subset(set1 & set2)}")
    print(f"(s1 & s2) subset of Set2: {set2.subset(set1 & set2)}")
    print(f"(s1 | s2) subset of Set1: {set1.subset(set1 | set2)}")
    print(f"Set1 subset of (s1 | s2): {(set1 | set2).subset(set1)}")

def simplified_set_list(list_from_set: List[ColorShape]) -> List[str]:
    output:List[str] = []
    for cs in list_from_set:
        output.append(f"{cs.__letter__} {cs.__shape_type__}")
    return output

def test_advanced_methods_for_both_set_types():
    print ("Testing advanced methods for OpenAddressing")
    advanced_test_for_two_sets(OpenAddressingSet(), OpenAddressingSet())
    print("="*40)
    print("Testing advanced methods for Chained")
    advanced_test_for_two_sets(ChainedSet(), ChainedSet())

if __name__ == '__main__':
    # You probably only want one of these three at a time:

    demo_drawing()
    # basic_testing()  # tests methods in basic test. Also handy for testing resizing/refactoring.
    # test_advanced_methods_for_both_set_types()