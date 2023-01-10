#!/usr/bin/env python3
'''defines async_generator function'''
import asyncio
import random


async def async_generator() -> float:
    '''
    returns:
        random float
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        rand_result = random.randint(0, 10)
        yield rand_result
