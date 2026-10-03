import asyncio
import aiohttp
from bs4 import BeautifulSoup
import csv
import re


def scrap_and_save_links(text):
    soup = BeautifulSoup(text, "html.parser")

    with open("csv_file.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        for link in soup.find_all(
            "a",
            attrs={"href": re.compile("http")}
        ):
            writer.writerow([link.get("href")])


async def fetch(session, url):
    try:
        async with session.get(url) as response:
            text = await response.text()
            scrap_and_save_links(text)
            print(url, response.status)

    except Exception as e:
        print(f"Error with {url}: {e}")


async def scrap(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch(session, url)
            for url in urls
        ]

        await asyncio.gather(*tasks)


urls = [
    "https://analytics.usa.gov/",
    "https://www.python.org/",
    "https://www.linkedin.com/"
]


asyncio.run(scrap(urls))