import requests
import json
import asyncio
import aiohttp

async def sbin(title: str, dec: str):
    json_data = {
        'title': title,
        'files': [
            {
                'content': dec,
            },
        ],
    }
    async with aiohttp.ClientSession() as session:
        async with session.post("https://sourceb.in/api/bins", json=json_data) as response:
            return f"https://sourceb.in/{json.loads(await response.text())["key"]}"

async def run():

    aw = await sbin("HelloWorld", "print('HelloWorld')")

    print(aw)

asyncio.run(run())