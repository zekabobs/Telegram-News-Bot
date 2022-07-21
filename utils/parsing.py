import aiohttp
import asyncio
from bs4 import BeautifulSoup

site = 'https://izhevsk.mk.ru/news/'


async def to_parse():
    async with aiohttp.ClientSession() as session:
        async with session.get(site) as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')

                link = soup.find('li', class_='news-listing__item').findChild('a')
                new_link = link['href']

                async with session.get(new_link) as new_response:
                    new_html = await new_response.text()
                    new_soup = BeautifulSoup(new_html, 'html.parser')


                    main_tag = new_soup.find('main')
                    news_img = main_tag.find('figure', class_='article__picture-group').findChild('img')['src']
                    news_text = main_tag.find('div', class_='article__body').findChildren('p')
                    news_article = f'<b>{news_text[0].text}</b>'
                    for prh in news_text[1:]:
                        news_article += '\n\n' + prh.text
                    print(news_article)

                    return {'img': news_img, 'article': news_article}


async def main():
    task = asyncio.create_task(to_parse())
    await task


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
