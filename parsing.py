from aiohttp import request
from bs4 import BeautifulSoup
import asyncio


# url = https://izhlife.ru/news/?ysclid=l5kzdaa3zr146348059


async def parse():
    html = request(url="https://izhlife.ru/news/?ysclid=l5kzdaa3zr146348059")
    soup = BeautifulSoup(request(html, 'html.parser'))
