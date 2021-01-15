from backend.controllers.base_controller import BaseController
from backend.dao.db.marketplace_dao import MarketplaceDao


class MarketplaceController(BaseController):
    def __init__(self):
        self.__dao = MarketplaceDao()
        super().__init__(self.__dao)