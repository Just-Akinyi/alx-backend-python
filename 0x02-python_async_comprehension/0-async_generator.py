#!/usr/bin/env python3
'''defines async_generator function'''
import asyncio
import random
from typing import List


async def async_generator() -> List[float]:
    '''
    returns:
        random float
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
