#!/usr/bin/env python3
"""Module contains function that returns sum of list items

Imports:
    typing: Module contains List annotation type
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    for f in input_list:
        f += f
    return f
