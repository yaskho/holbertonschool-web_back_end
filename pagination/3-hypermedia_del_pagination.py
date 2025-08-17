#!/usr/bin/env python3
def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
    """Return a page of the dataset with deletion-resilient hypermedia pagination.

    Args:
        index (int): the starting index of the page
        page_size (int): the number of items to return

    Returns:
        Dict: dictionary containing the page data, current index,
              next index, and actual page size
    """
    assert isinstance(index, int) and 0 <= index, "Index must be a non-negative integer"
    assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"

    indexed = self.indexed_dataset()
    all_keys = sorted(indexed.keys())

    if index > all_keys[-1]:
        raise AssertionError("Index out of range")

    data = []
    current_index = index
    count = 0
    # Iterate through sorted keys starting from 'index'
    for key in all_keys:
        if key >= index:
            data.append(indexed[key])
            count += 1
            if count == page_size:
                break

    # Determine next_index
    remaining_keys = [k for k in all_keys if k > current_index]
    if count > 0:
        next_index = remaining_keys[count - 1] + 1 if count <= len(remaining_keys) else None
    else:
        next_index = None

    return {
        "index": index,
        "next_index": next_index,
        "page_size": len(data),
        "data": data
    }
