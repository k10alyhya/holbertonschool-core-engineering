#!/usr/bin/env python3
"""
This module contains the VerboseList class which extends Python's built-in
list class to provide printed notifications for modifying operations.
"""


class VerboseList(list):
    """
    A custom list class that prints notification messages whenever items
    are added or removed from the list.
    """

    def append(self, item):
        """
        Adds an item to the end of the list and prints a notification.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """
        Extends the list by appending elements from the iterable and
        prints a notification with the count of added items.
        """
        items = list(iterable)
        count = len(items)
        super().extend(items)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """
        Prints a notification message before removing the specified item.
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """
        Prints a notification message before popping an item at the given index.
        Defaults to popping the last item if no index is provided.
        """
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
