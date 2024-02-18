import aiofiles
import aiohttp
import asyncio
import time
import os
from bs4 import BeautifulSoup

base_url = 'https://parsinger.ru/asyncio/aiofile/3/'


async def write_file(session, url_img, name_img):
    async with aiofiles.open(f'images/{name_img}', mode='wb') as f:
        async with session.get(url_img) as response:
            async for x in response.content.iter_chunked(2048):
                await f.write(x)
                print(f'{name_img} скачано')


async def main():
    images = []
    async with aiohttp.ClientSession() as session:
        async with session.get(url=base_url) as response:
            soup = BeautifulSoup(await response.text(), 'lxml')
            links = [base_url + link['href'] for link in soup.find_all('a')]
            for link in links:
                async with session.get(url=link) as resp1:
                    soup1 = BeautifulSoup(await resp1.text(), 'lxml')
                    links1 = [link.split('category')[0] + link1['href'] for link1 in soup1.find_all('a')]
                    for link1 in links1:
                        async with session.get(url=link1) as resp2:
                            soup2 = BeautifulSoup(await resp2.text(), 'lxml')
                            [images.append(link2['src']) for link2 in soup2.find_all('img') if
                             link2['src'] not in images]
        await asyncio.gather(*[write_file(session, img, img.split('/')[-1]) for img in images])


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
