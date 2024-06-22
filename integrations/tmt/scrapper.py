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
            content = await page.content()
            print(url, content)

            # hrefs = await page.evaluate('''() => {
            #     let hrefs = [];
            #     let links = document.querySelectorAll('a');
            #     links.forEach(link => {
            #         hrefs.push(link.href);
            #     });
            #     return hrefs;
            # }''')

            # print('Hrefs de los enlaces:', hrefs)
