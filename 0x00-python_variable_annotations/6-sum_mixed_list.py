#!/usr/bin/env python3
''' type-annotated function sum_list'''
from typing import List


def sum_mixed_list(mxd_lst: List[float | int]) -> float:
    '''
    Args:
        input_list: list[float | int]
    Return:
        float
    '''
    return sum(mxd_lst)
