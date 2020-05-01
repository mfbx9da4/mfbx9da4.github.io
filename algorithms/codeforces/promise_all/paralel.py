from typing import NamedTuple
import aiohttp
import asyncio
import math


class Response(NamedTuple):
    status: str
    text: str


async def fetch(session, url):
    async with session.get(url) as response:
        return Response(**{'status': response.status,
                           'text': await response.text()})


async def promise_all(*tasks):
    return await asyncio.gather(*tasks)


async def randomText(text='text'):
    await asyncio.sleep(1 * math.random())
    return text


async def main():
    urls = [
        'http://python.org',
        'https://google.com',
        'https://davidalbertoadler.com'
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        responses = await promise_all(*tasks)
        for i, response in enumerate(responses):
            print(urls[i], response.status)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
