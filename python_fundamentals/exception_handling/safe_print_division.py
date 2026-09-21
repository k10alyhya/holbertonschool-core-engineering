#!/usr/bin/env python3


def safe_print_division(a, b):
    """Safely divide two numbers and print the result."""
    result = None

    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        pass
    finally:
        print("Inside result: {}".format(result))

    return result
