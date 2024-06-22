from pyppeteer import launch
from pyppeteer.network_manager import Response


class VisitPageContext:
    browser = None

    def __init__(self, url: str):
        self.url = url

    async def __aenter__(self) -> Response:
        self.browser = await launch()
        page = await self.browser.newPage()
        await page.goto(self.url)
        return page

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.browser.close()
