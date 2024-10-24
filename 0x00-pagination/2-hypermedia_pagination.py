#!/usr/bin/env python3
"""
2-hypermedia_pagination.py
"""
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''Return tuple containing pagination start index and end index.'''
    return ((page_size * (page - 1)), page_size * page)


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
        """
        Takes the page index and page_size and returns the page contents paged
        on the indices form the dataset
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()
        if start >= len(dataset):
            return []
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, List]:
        ''' Return dict of pagination data.
            Dict key/value pairs consist of the following:
                page_size - length of dataset page
                page - current page number
                data - dataset page
                next_page - number of next page if there is one
                prev_page - number of previous page if there is one
                total_pages - total number of pages '''
        page_content = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset())/page_size)
        return {
            'page_size': len(page_content),
            'page': page,
            'data': page_content,
            'next_page': page + 1 if page <= total_pages - 1 else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages,
           }
