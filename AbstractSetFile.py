from abc import ABC, abstractmethod


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

    @abstractmethod
    def remove(self, item):
        """
        attempts to remove item from this set. If item was not in the set, returns False. Otherwise, returns True.
        :param item: item to remove
        :return: whether we have removed the value, decrementing the size of the set by one.
        """
        pass

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
    def subset(self, other: BasicAbstractSet) -> bool:
        """
        indicates whether ALL of the items in the other set are contained within this one.
        :param other: another set that might have items overlapping with this one.
        :return: whether the "other" set is entirely contained in this one.
        """
        pass
