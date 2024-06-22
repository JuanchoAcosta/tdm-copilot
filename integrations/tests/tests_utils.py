from django.test import TestCase

from integrations.tmt.utils import TmtUtils


class TmtUtilsTest(TestCase):

    def test_get_page_number_from_url(self):
        url = "https://www.tenisdemesaparatodos.com/ranking.asp?pagina=27"

        utils = TmtUtils()

        result = utils.get_page_number_from_url(url=url)

        expected_result = 27

        assert result == expected_result
