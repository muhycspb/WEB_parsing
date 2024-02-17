import aiofiles
import aiohttp
import asyncio
import time
import os
from bs4 import BeautifulSoup

base_url = 'https://parsinger.ru/asyncio/aiofile/2/'


async def write_file(session, url, name_img):
    async with aiofiles.open(f'images/{name_img}', mode='wb') as f:
        async with session.get(url) as response:
            async for x in response.content.iter_chunked(1024):
                await f.write(x)


async def run_tasks(session, link):
    async with session.get(url=link) as resp:
        soup = BeautifulSoup(await resp.text(), 'lxml')
        images = [img['src'] for img in soup.find_all('img')]
        for img in images:
            await write_file(session, img, img.split('/')[-1])


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(url=base_url) as resp:
            soup = BeautifulSoup(await resp.text(), 'lxml')
            links_list = [base_url + a['href'] for a in soup.find_all('a')]
            tasks = [asyncio.create_task(run_tasks(session, link)) for link in links_list]
            await asyncio.gather(*tasks)


def get_folder_size(filepath, size=0):
    for root, dirs, files in os.walk(filepath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
    return size


if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    start = time.time()
    asyncio.run(main())
    print(time.time() - start)
    print(get_folder_size('images'))
