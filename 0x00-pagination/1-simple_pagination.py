#!/usr/bin/env python3
"""
This module implements basic pagination for a dataset containing
popular baby names.
"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for retrieving a specific page of data.

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
    Server class to paginate a database of popular baby names.

    This class loads a dataset from a CSV file and provides a method
    to retrieve a specific page of records.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the Server with an empty dataset cache."""
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
            self.__dataset = dataset[1:]  # Skip the header row
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a specific page of data.

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
