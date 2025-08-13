#!/usr/bin/env python3

import csv
from typing import List, Dict


class Server:

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # skip header
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:

        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        assert isinstance(index, int) and index >= 0,
        assert isinstance(page_size, int) and page_size > 0,

        indexed_data = self.indexed_dataset()
        assert index < len(indexed_data),

        data = []
        current_index = index
        while len(data) < page_size and current_index < max(indexed_data.keys()) + 1:
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
            current_index += 1

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": current_index
        }
