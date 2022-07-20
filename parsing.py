import aiohttp
import asyncio
from bs4 import BeautifulSoup

site = 'https://udm-info.ru/'


async def parse():
    async with aiohttp.ClientSession() as session:
        async with session.get(site) as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')

                link = soup.find('div', class_='secondary').findChild('a')
                section = soup.find('section', class_='cols')
                news_img = section.findChild('img')['src']

                new_link = site + link['href']

                async with session.get(new_link) as new_response:
                    new_html = await new_response.text()
                    new_soup = BeautifulSoup(new_html, 'html.parser')

                    section = new_soup.find('section', class_='cols')
                    news_title = section.find('div', class_='cm-subtitle').text
                    news_pargh = section.find('div', class_='paragraph').text
                    return {'img': news_img, 'title': news_title, 'pargh': news_pargh}


async def main():
    task = asyncio.create_task(parse())
    await task


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
