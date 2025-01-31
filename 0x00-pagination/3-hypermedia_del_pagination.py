#!/usr/bin/env python3
"""
Deletion-Resilient Hypermedia Pagination

This module provides functionality for paginating a dataset of
popular baby names while ensuring resilience to deletions.
"""

import csv
import math
from typing import Dict, List


class Server:
    """
    Server class to paginate a dataset of popular baby names.

    This class loads a dataset from a CSV file and provides methods
    to retrieve paginated data with an indexed approach, ensuring
    robustness even if records are deleted.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the server with empty dataset caches."""
        self.__dataset = None
        self.__indexed_dataset = None

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

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Create and cache an indexed dataset for efficient pagination.

        The dataset is stored as a dictionary where the keys represent
        the original index positions, allowing for deletion resilience.

        Returns:
            Dict[int, List]: A dictionary mapping index positions to records.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieve a page of data using index-based pagination, ensuring
        resilience to deletions.

        Args:
            index (int, optional): The starting index for the page. Defaults to 0.
            page_size (int): The number of records per page.

        Returns:
            Dict: A dictionary containing:
                - 'index': The starting index of the current page.
                - 'next_index': The starting index for the next page, or None if at the end.
                - 'page_size': The number of records in the current page.
                - 'data': The list of records for the current page.
                - 'total_pages': The total number of pages available.

        Raises:
            AssertionError: If the index is out of range.
        """
        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)

        # Default to the first index if not provided
        if index is None:
            index = 0

        assert 0 <= index < len(dataset), "Index out of range."

        start_index = index
        end_index = min(index + page_size, len(dataset))
        data = dataset[start_index:end_index]

        # Determine the next index for pagination
        next_index = end_index if end_index < len(dataset) else None

        return {
            "index": start_index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data,
            "total_pages": total_pages,
        }
