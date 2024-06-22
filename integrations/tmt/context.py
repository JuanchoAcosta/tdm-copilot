from pyppeteer import launch
from pyppeteer.network_manager import Response


class VisitPageContext:
    GOTO_TIMEOUT = 60000

    browser = None
    page = None

    def __init__(self, url: str):
        self.url = url

    async def __aenter__(self) -> Response:
        """Open a browser and visit the page"""
        self.browser = await launch()
        self.page = await self.browser.newPage()
        await self.page.goto(self.url, {'timeout': self.GOTO_TIMEOUT})
        return self.page

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.page.close()
        await self.browser.close()
