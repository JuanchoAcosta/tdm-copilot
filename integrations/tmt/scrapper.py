from .context import VisitPageContext

class TMTScrapperService:

    async def get_ranking_page(self, page_number: int) -> int:
        base_url = "https://www.tenisdemesaparatodos.com/ranking.asp/ranking.asp?pagina="
        url = f"{base_url}{page_number}"

        async with VisitPageContext(url) as page:

            href = await page.evaluate('''() => {
                const link = document.querySelector('a');
                return link ? link.href : null;
            }''')

            print('Href del enlace:', href)
