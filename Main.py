import asyncio
import aiohttp
from bs4 import BeautifulSoup
import platform
import time
import os
import random
from colorama import Fore, Style

hwid = platform.node()

def Delay(Time, Message):
    os.system('cls')
    print(Message)
    print(f"{Fore.YELLOW}Waiting... [{Time}s]")
    time.sleep(Time)

async def main():

    hwid = hex(random.randint(10000000000 * 10^8, 99999999999 * 10^8)) * 3 # it doesn't actually matter what you put for this lul

    urls = [
        [
            f"https://flux.li/windows/start.php?updated_browser=true&HWID={hwid}",
            None
        ],
        [
            "https://fluxteam.net/windows/checkpoint/check1.php",
            "https://linkvertise.com/152666/fluxus-windows-check-1/1"
        ],
        [
            "https://fluxteam.net/windows/checkpoint/check2.php",
            "https://linkvertise.com/152666/fluxus-windows-check-2/1"
        ],
        [
            "https://fluxteam.net/windows/checkpoint/main.php",
            "https://linkvertise.com/152666/fluxus-windows-main/1"
        ]
    ]

    tasks = [request(url[0], url[1]) for url in urls]
    responses = await asyncio.gather(*tasks)

    for response in responses:
        os.system('cls')
        Delay(0, f"{Style.RESET_ALL}Loaded {Fore.BLUE}{response.url}.")

    document = BeautifulSoup(responses[-1].content, "html.parser")
    key_element = document.select_one("main code:nth-of-type(2)")
    key = key_element.get_text(strip=True) if key_element else False

    os.system('cls')

    if key:
        print(f"\n{Style.RESET_ALL}Your key is: {Fore.GREEN}{key}\n{Style.RESET_ALL}Press enter to exit...")
    else:
        print(f"{Style.RESET_ALL}{Fore.RED}Sorry, your key could not be retreived, try waiting a bit.\n{Style.RESET_ALL}Press enter to exit.", end="")
    
    print(Style.RESET_ALL)
    input()

async def request(url, referrer):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
    }
    if referrer:
        headers["Referer"] = referrer
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as response:
            content = await response.text()
            return Response(url, content)

class Response:
    def __init__(self, url, content):
        self.url = url
        self.content = content

asyncio.run(main())