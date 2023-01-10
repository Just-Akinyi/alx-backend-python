#!/usr/bin/env python3
'''defines measure_runtime function'''
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    returns:
        float
    '''
    start_time = asyncio.get_running_loop().time()
    await asyncio.gather(
        *(async_comprehension() for _ in range(4))
    )
    end_time = asyncio.get_running_loop().time()
    return end_time - start_time
