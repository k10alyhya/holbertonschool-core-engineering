#!/usr/bin/env python3


def best_score(a_dictionary):
    """Return the key with the highest score."""
    best_value = None
    best_key = None

    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    for key, value in a_dictionary.items():
        if best_value is None or best_value < value:
            best_value = value
            best_key = key

    return best_key
