#!/usr/bin/env python3
"""
This module defines a function to calculate the start and end index
for paginating a dataset given the page number and page size.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for a given page and page size.

    Args:
        page (int): The current page number (1-based index).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index (inclusive)
        and end index (exclusive) for retrieving items from a dataset.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
