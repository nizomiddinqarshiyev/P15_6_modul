from celery import Celery
from playwright.async_api import async_playwright


celery = Celery(
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0',
)


@celery.task()
async def screenshot_task():
    async with async_playwright() as playwright:

        browser = await playwright.firefox.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto('https://kun.uz/news/category/jahon')
        await page.screenshot(path='news.png')
















