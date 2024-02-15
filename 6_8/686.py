import aiohttp
import asyncio
import time
from bs4 import BeautifulSoup

url = 'https://parsinger.ru/asyncio/create_soup/1/'
summ = []


async def run_tasks(session, link):
    async with session.get(url=link) as resp:
        soup = BeautifulSoup(await resp.text(), 'lxml')
        p = soup.find('p').text
        if p.isdigit():
            summ.append(int(p))


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as resp:
            soup = BeautifulSoup(await resp.text(), 'lxml')
            links_list = [url + a['href'] for a in soup.find_all('a')]
            tasks = [asyncio.create_task(run_tasks(session, link)) for link in links_list]
            await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    start = time.time()
    asyncio.run(main())
    print(sum(summ))
    print(time.time() - start)
