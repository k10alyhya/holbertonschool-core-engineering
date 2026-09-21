#!/usr/bin/env python3


def safe_print_integer(value):
    """Safely print an integer."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
