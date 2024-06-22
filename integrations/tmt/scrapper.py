
from .context import VisitPageContext
from .utils import TmtUtils


class TmtScrapperService:
    base_url = "https://www.tenisdemesaparatodos.com"

    def __init__(
        self,
        utils: TmtUtils
    ):
        self._utils = utils

    async def get_ranking_page(self, page_number: int) -> int:
        url = f"{self.base_url}/ranking.asp?pagina={page_number}"

        async with VisitPageContext(url) as page:

            return page

    async def get_total_ranking_pages(self):
        url = f"{self.base_url}/ranking.asp"

        async with VisitPageContext(url) as page:
            links = await page.evaluate('''() => {
                let links = [];
                let anchors = document.querySelectorAll('a');
                anchors.forEach(link => {
                    links.push(link.href);
                });
                return links;
            }''')

            filtered_href = [
                link for link in links
                if '/ranking.asp?pagina=' in link
            ]

            looked_for_href = filtered_href[-2] # last one is the next page

            max_page_number = self._utils.get_page_number_from_url(
                url=looked_for_href,
            )

            return max_page_number
