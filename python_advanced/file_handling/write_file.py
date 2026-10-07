#!/usr/bin/env python3
"""Module that writes a string to a text file."""


def write_file(filename="", text=""):
    """Write text to a UTF-8 file and return the number of chars written."""
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
