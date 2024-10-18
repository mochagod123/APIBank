import aiohttp
import re
from bs4 import BeautifulSoup

async def GetItemID(url: str):
    if re.match(r'https://www.amazon.co.jp/\S+/dp/', url):
        id = url.split("/")
        return id[5]
    else:
        return

async def GetItemName(id: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://sakura-checker.jp/search/{id[5]}/") as response:
            soup = BeautifulSoup(await response.text(), 'html.parser')
            base = soup.find_all('section', {'class', "mainBlock"})[0]
            name = base.find_all("div", {"class", "item-title"})[0]
            return name.get_text()

async def GetItemIcon(id: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://sakura-checker.jp/search/{id[5]}/") as response:
            soup = BeautifulSoup(await response.text(), 'html.parser')
            base = soup.find_all('section', {'class', "mainBlock"})[0]
            icon = base.find_all("div", {"class", "item-review-wrap"})[0].find_all("img")[0]
            return icon["src"]
        
async def GetItemSakuraIcon(id: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://sakura-checker.jp/search/{id[5]}/") as response:
            soup = BeautifulSoup(await response.text(), 'html.parser')
            base = soup.find_all('section', {'class', "mainBlock"})[0]
            pa = base.find_all("div", {"class", "chartBlock mg-top15"})[0]
            pai = pa.find_all("img")[0]
            return pai["src"]