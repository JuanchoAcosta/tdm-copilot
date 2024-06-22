import asyncio
from datetime import datetime
from django.core.management.base import BaseCommand

from integrations.tmt.factory import TmtScrapperFactory


class Command(BaseCommand):
    help = 'Description of your command'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **kwargs):
        asyncio.run(main())

async def main():
    start_time = datetime.now()
    print(f"Start time: {start_time}")
    scrapper = TmtScrapperFactory().build_scrapper()
    max_page = await scrapper.get_total_ranking_pages()

    print(f"Max pages: {max_page}")

    offset = 1
    pages_calls = [
        scrapper.get_ranking_page(page_number=i)
        for i in range(offset, max_page + offset)
    ]
    responses = await asyncio.gather(*pages_calls)

    print(f"All responses: {len(responses)}")

    end_time = datetime.now()
    print(f"End time: {end_time}")
    print(f"Total time: {end_time - start_time}")
