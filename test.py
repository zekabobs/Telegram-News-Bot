import aiohttp
import asyncio
from bs4 import BeautifulSoup


async def parse():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://izhlife.ru/news/?ysclid=l5kzdaa3zr146348059') as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print(html)
            soup = BeautifulSoup(html, 'html.parser')
            ul = soup.findAll("a", attrs={'class': 'material-card__link'})
            print(ul)


async def main():
    task = asyncio.create_task(parse())
    await task


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
