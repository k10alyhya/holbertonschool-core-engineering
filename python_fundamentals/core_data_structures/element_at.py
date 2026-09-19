#!/usr/bin/env python3

def element_at(my_list, idx):
    """Return an element safely from a list."""
    if idx < 0:
        return None
    elif idx >= len(my_list):
        return None
    else:
        return my_list[idx]
