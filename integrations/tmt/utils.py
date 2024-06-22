import re as regular_expressions


class TmtUtils:

    def get_page_number_from_url(self, url: str) -> int:
        pattern = r"pagina=(\d+)&"
        match = regular_expressions.search(pattern, url)

        return int(match.group(1))
