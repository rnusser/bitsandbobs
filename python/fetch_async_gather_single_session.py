import requests
import asyncio
from aiohttp import ClientSession

base = "https://swapi.dev/api/"
person = "people/"

async def get_person(session, url):
    info = await session.request(method="GET", url=url)
    info.raise_for_status()
    data = await info.json()
    return data["name"]


async def main():
    tasks = []
    async with ClientSession() as session:
        for id in range(1,5):
            url = base + person + str(id) + '/'
            tasks.append(get_person(session, url))

        results = await asyncio.gather(*tasks)
    print(results)

if __name__ == "__main__":
    asyncio.run(main())




