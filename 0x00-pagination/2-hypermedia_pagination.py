#!/usr/bin/env python3
"""
This module provides functionality for paginating a dataset of
popular baby names, including hypermedia-style pagination metadata.
"""

import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Compute the start and end index for a given page and page size.

    Args:
        page (int): The current page number (1-based index).
        page_size (int): The number of records per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index (inclusive)
        and end index (exclusive) for slicing the dataset.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """
    Server class to paginate a dataset of popular baby names.

    This class loads a dataset from a CSV file and provides methods
    to retrieve paginated data along with hypermedia pagination metadata.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the server with an empty dataset cache."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Load and cache the dataset from the CSV file.

        Returns:
            List[List]: A list of records (each record is a list of values).
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclude the header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a specific page of data from the dataset.

        Args:
            page (int): The page number to retrieve (1-based index).
            page_size (int): The number of records per page.

        Returns:
            List[List]: A list of records for the requested page.
            Returns an empty list if the page is out of range.

        Raises:
            AssertionError: If page or page_size is not a positive integer.
        """
        assert isinstance(page, int) and isinstance(page_size, int),
        assert page > 0 and page_size > 0,

        start, end = index_range(page, page_size)
        data = self.dataset()

        if start >= len(data):  # Ensure start index is within dataset range
            return []

        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Retrieve a page of data along with hypermedia pagination metadata.

        Args:
            page (int): The page number to retrieve (1-based index).
            page_size (int): The number of records per page.

        Returns:
            Dict: A dictionary
        """
        data = self.get_page(page, page_size)
        start, end = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if end < len(self.__dataset) else None,
            'prev_page': page - 1 if start > 0 else None,
            'total_pages': total_pages
        }
