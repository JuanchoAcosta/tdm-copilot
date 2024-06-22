from .scrapper import TmtScrapperService
from .utils import TmtUtils


class TmtScrapperFactory:

    def build_scrapper(self,) -> TmtScrapperService:
        utils = TmtUtils()

        return TmtScrapperService(
            utils=utils,
        )
