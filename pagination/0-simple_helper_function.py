#!/usr/bin/env python3
"""
0-simple_helper_function: Provides a helper function to calculate
the start and end index for pagination based on page and page_size.
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Return a tuple containing the start and end index for
    a list corresponding to the given page and page_size.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
