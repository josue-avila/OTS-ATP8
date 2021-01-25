from backend.dao.db.base_dao import BaseDao
from backend.models.marketplace import Marketplace


class MarketplaceDao(BaseDao):
    def __init__(self):
        super().__init__(Marketplace)
