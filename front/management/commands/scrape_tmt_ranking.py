import asyncio
from django.core.management.base import BaseCommand

from integrations.tmt.scrapper import TMTScrapperService


class Command(BaseCommand):
    help = 'Description of your command'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **kwargs):
        scrapper = TMTScrapperService()
        asyncio.run(scrapper.get_total_ranking_pages())
