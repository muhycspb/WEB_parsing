import asyncio
import time
import aiohttp
from bs4 import BeautifulSoup

category = ['watch', 'mobile', 'mouse', 'hdd', 'headphones']
urls = [f'https://parsinger.ru/html/{cat}/{i}/{i}_{x}.html' for cat, i in zip(category, range(1, len(category) + 1)) for
        x in range(1, 33)]

sum_discount = 0


async def run_tasks(url, session):
    async with session.get(url) as resp:
        global sum_discount
        soup = BeautifulSoup(await resp.text(), 'lxml')
        price = int(soup.find('span', id='price').text.split()[0])
        old_price = int(soup.find('span', id='old_price').text.split()[0])
        stock = int(soup.find('span', id='in_stock').text.split()[-1])
        sum_discount += (old_price - price) * stock


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [run_tasks(link, session) for link in urls]
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    start = time.time()
    asyncio.run(main())
    print(time.time() - start)
    print(sum_discount)