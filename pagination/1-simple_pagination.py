#!/usr/bin/env python3
"""Module contains function that returns pagination range
Imports:
    Tuple: Tuple type annotation
    List: List type anotaton
    csv: csv module
"""
import csv
from typing import List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Gets specific data
        """
        assert page > -1
        assert page > 0 and isinstance(page, int)
        assert page_size > 0 and isinstance(page_size, int)
        myRange = index_range(page, page_size)
        start: int = myRange[0]
        end: int = myRange[1]
        filtered_list: list = self.dataset()

        if start >= len(filtered_list):
            return []
        return filtered_list[start:end]
