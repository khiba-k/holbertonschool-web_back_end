#!/usr/bin/env python3
"""Module contains function that returns pagination range
Imports:
    Tuple: Tuple type annotation
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Function returns pagination range

    Args:
        page (int): page number
        page_size (int): page size

    Returns:
        Tuple[int, int]: start to end range
    """
    start = 15 * (page - 1)
    end = start + page_size

    return ((start, end))
