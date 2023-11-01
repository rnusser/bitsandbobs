import requests
import asyncio
from aiohttp import ClientSession
import json

base = "https://swapi.dev/api/"
person = "people/"


async def get_person(id) -> dict:
    async with ClientSession() as session:
        async with session.request(method="GET", url=base + person + str(id) + "/") as response:
            return (response.headers, await response.text(), response.status)


async def main():
    tasks = []
    for id in range(1, 5):
        tasks.append(get_person(id))

    results = await asyncio.gather(*tasks)

    for result in results:
        headers, text, status = result
        myjson = json.loads(text)
        print(myjson.get("name"))


if __name__ == "__main__":
    asyncio.run(main())
