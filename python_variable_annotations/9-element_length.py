#!/usr/bin/env python3
"""Module contains function that return list
"""
from typing import List, Tuple, Sequence


def element_length(lst: list) -> List[Tuple[Sequence[int]]]:
    """Function returns list

    Args:
        lst (list): list to be iterated through

    Returns:
        List[Tuple[Sequence[int]], int]: Returned List
    """
    return [(i, len(i)) for i in lst]
