from typing import NamedTuple
import asyncio
from random import random
from time import perf_counter as now


# Task consists of future and coroutine
# Futures are variables you can attach a callback to when set
# Coroutines are like generators. Coroutines yield Futures.
# await syntax is equivalent to a yield
# Task is like a mini generator + future instance.
# A task is a future associated with some active event loop.
# The mini event loop is known as the task executor.


async def randomText(text, delay):
    print('>>', text, 'delay', delay)
    await asyncio.sleep(delay)
    print('||', text, 'delay', delay)
    return text


async def timer(task):
    start = now()
    res = await task
    end = now()
    return (end-start, res)


async def last_task(*tasks):
    responses = await asyncio.gather(*map(timer, tasks))
    print('responses', responses)
    return min(responses)[1]


async def main():
    tasks = [randomText(i,  random()) for i in range(3)]
    res = await last_task(*tasks)
    print(res)

if __name__ == '__main__':
    asyncio.run(main())
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
