import asyncio
import string
import random
import time
import logging

import aiohttp

from settings import APP_URL


def create_random_string(length):
    characters = string.ascii_letters + string.digits
    text = "".join(random.choice(characters) for _ in range(length))
    return text


async def create_posts(length: int = 16):
    async with aiohttp.ClientSession(base_url=f"{APP_URL}") as session:
        for _ in range(random.randint(10, 100)):
            text = create_random_string(length=length)
            async with session.post(f"/post/new?text={text}"):
                pass


async def get_count_posts(count: int = 10) -> list | None:
    async with aiohttp.ClientSession(base_url=f"{APP_URL}") as session:
        response = await session.get(f"/post/all/{count}")
        if response.status == 200:
            all_data = await response.json()
            result = [data["uuid"] for data in all_data]
            return result
        return None


async def delete_current_posts(data: list) -> int | None:
    counter = 0
    async with aiohttp.ClientSession(base_url=f"{APP_URL}") as session:
        for uuid in data:
            async with session.delete(f"/post/{uuid}") as resp:
                if resp.status == 200:
                    counter += 1
    return counter if counter > 0 else None


async def main():
    logging.basicConfig(
        format='INFO: [clientapp] %(asctime)s - %(message)s',
        level=logging.INFO
    )
    logging.info("The client has been started")
    await create_posts()
    total = 0
    iterations = 0
    while True:
        counter = 0
        time.sleep(10)
        data = await get_count_posts()
        if data:
            result = await delete_current_posts(data=data)
            counter += result
            total += result
        else:
            logging.info(f"Total posts deleted {total}")
            break
        iterations += 1
        logging.info(f"Iteration № {iterations}: "
                     f"posts have been deleted {counter}.")


if __name__ == "__main__":
    asyncio.run(main())
