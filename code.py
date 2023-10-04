import os
import requests
import asyncio
from dotenv import load_dotenv
load_dotenv()
from playwright.async_api import async_playwright


async def play(username, password):
    async with async_playwright() as playwright:
        browser = await playwright.firefox.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto('https://www.instagram.com/accounts/login/?source=auth_switcher')
        await page.get_by_label("Phone number, username, or email").fill(username)
        await page.get_by_label("Password").fill(password)
        await page.get_by_role('button', name='Log in', exact=True).click()
        await page.wait_for_timeout(3000)
        await page.get_by_alt_text(f"{username}'s profile picture").click()
        await page.get_by_role("link", name="Clip").first.click()
        await page.wait_for_timeout(1000)
        await page.screenshot(path='post_one.png')
        await browser.close()


async def kun_uz_play():
    async with async_playwright() as playwright:
        browser = await playwright.firefox.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto('https://kun.uz/news/category/jahon')
        await page.screenshot(path='news.png', full_page=False)
        # await page.get_by_role('link', name='19:49 / 28.09.2023', exact=True).click()
        # await page.inner_text('news.txt')
        # await page.get_by_role('link', name='''19:49 / 28.09.2023 Қодиров атрофида янги можаро: унинг ўғли Қуръонни ёққан россияликни тергов қамоқхонасида калтаклаган
        # Чеченистон раҳбари ўғли билан фахрланишини айтди,
        # россияликлар эса ундан норози.''', exact=True).click()
        # print(await page.get_by_text('19:49 / 28.09.2023').inner_text())
        await page.wait_for_timeout(1000)


# asyncio.run(kun_uz_play())

# dat = asyncio.run(kun_uz_play())
# print(type(dat))
# for i in dat:
#     print(type(i))

# password = os.getenv('password')
# username = os.getenv('username')
# asyncio.run(play(username, password))


def get_temperature(lat, lon):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    appid = os.getenv('APIKEY')
    response = requests.get(url, params={
        'lat': lat,
        'lon': lon,
        'units': 'metric',
        'appid': appid
    })
    return response.json()


def get_address_using_location(lat, lon):
    url = "https://geocode-maps.yandex.ru/1.x/"
    params = {
        "apikey": "<api_key>",
        "geocode": f"{lon},{lat}",
        "lang": "en",
        "format": "json"
    }
    response = requests.get(url, params=params)
    data_p = response.json()
    print(data_p)
    city = data_p['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty'][
        'GeocoderMetaData']['Address']['formatted']
    return city





