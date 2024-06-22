import re as regular_expressions

from .context import VisitPageContext


class TMTScrapperService:
    base_url = "https://www.tenisdemesaparatodos.com"

    async def get_ranking_page(self, page_number: int) -> int:
        url = f"{self.base_url}/ranking.asp?pagina={page_number}"

        async with VisitPageContext(url) as page:

            href = await page.evaluate('''() => {
                const link = document.querySelector('a');
                return link ? link.href : null;
            }''')

            print('Href del enlace:', href)

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

            print('Looked for href:', looked_for_href)

            # Regex pattern to extract the page number
            pattern = r"pagina=(\d+)&"

            # Search for the pattern in the URL
            match = regular_expressions.search(pattern, looked_for_href)
            print("Match:", pattern, looked_for_href, match.group(1))

            return int(match.group(1))
