#!/usr/bin/env python3
''' type-annotated function sum_mixed_list'''
from typing import List,Union


def sum_mixed_list(mxd_lst: List[Union[float , int]]) -> float:
    '''
    Args:
        input_list: list[float | int]
    Return:
        float
    '''
    return sum(mxd_lst)
