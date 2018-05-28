#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time     : 2018/4/14 23:22
# @Author   : HYP
# @FileName : set源码.py
# @Software : PyCharm
list

class set(object):
    """
    set() -> new empty set object
    set(iterable) -> new set object

    Build an unordered collection of unique elements.
    """

    def add(self, *args, **kwargs):  # real signature unknown
        """
        Add an element to a set.

        This has no effect if the element is already present.
        """
        pass

    def clear(self, *args, **kwargs):  # real signature unknown
        """ Remove all elements from this set. """
        pass

    def copy(self, *args, **kwargs):  # real signature unknown
        """ Return a shallow copy of a set. """
        pass

    def difference(self, *args, **kwargs):  # real signature unknown
        """
        相当于 s1-s2
        Return the difference of two or more sets as a new set.

        (i.e. all elements that are in this set but not the others.)
        """
        pass

    def difference_update(self, *args, **kwargs):  # real signature unknown
        """ Remove all elements of another set from this set. """
        pass

    def discard(self, *args, **kwargs):  # real signature unknown
        """
        与 remove 功能相同，删除元素不存在时不会抛出异常；
        Remove an element from a set if it is a member.

        If the element is not a member, do nothing.
        """
        pass

    def intersection(self, *args, **kwargs):  # real signature unknown
        """
        相当于 s1&s2
        Return the intersection of two sets as a new set.

        (i.e. all elements that are in both sets.)
        """
        pass

    def intersection_update(self, *args, **kwargs):  # real signature unknown
        """ Update a set with the intersection of itself and another. """
        pass

    def isdisjoint(self, *args, **kwargs):  # real signature unknown
        """ Return True if two sets have a null intersection. """
        pass

    def issubset(self, *args, **kwargs):  # real signature unknown
        """
        相当于 s1 <= s2
        Report whether another set contains this set. """
        pass

    def issuperset(self, *args, **kwargs):  # real signature unknown
        """
        相当于 s1 >= s2
        Report whether this set contains another set. """
        pass

    def pop(self, *args, **kwargs):  # real signature unknown
        """
        Remove and return an arbitrary set element.
        Raises KeyError if the set is empty.
        """
        pass

    def remove(self, *args, **kwargs):  # real signature unknown
        """
        Remove an element from a set; it must be a member.

        If the element is not a member, raise a KeyError.
        """
        pass

    def symmetric_difference(self, *args, **kwargs):  # real signature unknown
        """
        相当于 s1^s2
        Return the symmetric difference of two sets as a new set.

        (i.e. all elements that are in exactly one of the sets.)
        """
        pass

    def symmetric_difference_update(self, *args, **kwargs):  # real signature unknown
        """ Update a set with the symmetric difference of itself and another. """
        pass

    def union(self, *args, **kwargs):  # real signature unknown
        """
        相当于 s1|s2

        Return the union of sets as a new set.

        (i.e. all elements that are in either set.)
        """
        pass

    def update(self, *args, **kwargs):  # real signature unknown
        """ Update a set with the union of itself and others. """
        pass