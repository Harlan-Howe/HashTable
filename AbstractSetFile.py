from abc import ABC, abstractmethod
from typing import List

MAX_LOAD_FACTOR = 0.75
MIN_LOAD_FACTOR = 0.1

class BasicAbstractSet(ABC):

    @abstractmethod
    def append(self, item) -> bool:
        """
        attempts to add item to this set. If item is already in this set, returns False and does not add
        another copy.
        :param item: the item to add
        :return: whether we successfully added item, meaning that the size of the set has increased by 1.
        """
        pass

    def __iadd__(self, other) -> "BasicAbstractSet":
        """
        A wrapper method for append, which allows us to use "+=" syntax with the set. (e.g., "mySet += item")
        Ignores the boolean return value of append.
        :param other: the item to attempt to add to this set.
        :return: this set, potentially including the added item.
        """
        # I've written this for you.
        self.append(other)
        return self

    @abstractmethod
    def remove(self, item):
        """
        attempts to remove item from this set, if it is in the set to remove. If item was not in the set, returns False.
        Otherwise, returns True.
        :param item: item to remove
        :return: whether we have removed the value, decrementing the size of the set by one.
        """
        pass

    # @abstractmethod
    # def is_a_match(self, index: int, object: ColorShape) -> bool:
    #     """
    #     RECOMMENDED BUT NOT REQUIRED - I just think this will be handy for you, because you might use it in more than
    #     one place. -- HH
    #     determines whether the given object is also stored at the given index in the hashtable
    #     :param index: which index might the object be stored?
    #     :param object: which object are we looking for?
    #     :return: whether object is already in the hash table at location index.
    #     """

    def __isub__(self, other):
        """
        wrapper method for remove... to implement "-=" syntax. (e.g., "mySet -= item")
        Ignores the boolean value returned by remove.
        :param other: the item to remove, if it is present.
        :return: this set, potentially with one fewer item in it.
        """
        # I've written this one for you.
        self.remove(other)
        return self

    @abstractmethod
    def __contains__(self, item) -> bool:
        """
        indicates whether item is already in the set.
        Note: you can call this dunder method by saying something like "if item in mySet:"
        :param item: the item to search for
        :return: True if the item was in the set, or False if it wasn't.
        """
        pass

    @abstractmethod
    def __len__(self) -> int:
        """
        get the number of items in the set
        Note: you can call this dunder method by saying something like "print (len(mySet))"
        :return: the number of items stored in the set.
        """
        pass

    @abstractmethod
    def get_load_factor(self) -> int:
        """
        determines the load factor (lambda) for this hash table.
        :return: the load factor... (num of items in the hash table)/(length of the hash table)
        """
        pass

    @abstractmethod
    def to_list(self) -> List:
        """
        creates a new list of the items in this Set, in no particular order. It should:
        a) be independent of the data storage for this list... that is, if the user changes something about the list
        returned, it should NOT alter this set.
        b) not include any of the "empty but searchable" items in the OpenAddressing set or Linked Lists in the
        resulting list.
        :return: A list of the items in this set.
        """


class AdvancedAbstractSet(BasicAbstractSet):

    @abstractmethod
    def __sub__(self, other: BasicAbstractSet) -> "AdvancedAbstractSet":
        """
        builds a new "DIFFERENCE" set out of the items in this set that aren't in the other set. This does not change
        this set.
        Note: you can call this dunder method by saying something like "diffSet = mySet - otherSet"
        :param other: another set that might have items overlapping with this one.
        :return: a new set containing those items in this set that aren't in the "other" one.
        """
        pass

    @abstractmethod
    def __and__(self, other: BasicAbstractSet) -> "AdvancedAbstractSet":
        """
        builds a new "INTERSECTION" set out of the items that are in BOTH this set and the "other" set. This does not
        change this set.
        Note: you can call this dunder method by saying something like "diffSet = mySet & otherSet"
        :param other: another set that might have items overlapping with this one.
        :return: a new set containing those items that are in BOTH sets.
        """
        pass

    @abstractmethod
    def __or__(self, other: BasicAbstractSet) -> "AdvancedAbstractSet":
        """
        builds a new "UNION" set out of the items that are in EITHER this set or the "other" one. This does not change
        this set.
        Note: you can call this dunder method by saying something like "diffSet = mySet | otherSet"
        :param other: another set that might have items overlapping with this one.
        :return: a new set containing those items that are in BOTH sets.
        """
        pass

    @abstractmethod
    def contains_all(self, other: BasicAbstractSet) -> bool:
        """
        indicates whether ALL of the items in the other set are contained within this one.
        :param other: another set that might have items overlapping with this one.
        :return: whether the "other" set is entirely contained in this one.
        """
        pass

    @abstractmethod
    def resize(self, desired_table_length: int) -> None:
        """
        builds a new Hash Table of the requested size and copies all the data from this set into it. Sets this new
        table as the table for this Set, replacing the old one.
        :param desired_table_length: The length of the List (or other structure) used to implement the hash table.
        :return: None
        """
        pass