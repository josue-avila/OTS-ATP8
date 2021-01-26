from backend.dao.db.base_dao import BaseDao
from backend.dao.db.marketplace_dao import MarketplaceDao


def test_marketplace_dao_instance():
    marketplace_dao = MarketplaceDao()

    assert isinstance(marketplace_dao, BaseDao)
    assert isinstance(marketplace_dao, MarketplaceDao)
    assert issubclass(MarketplaceDao, BaseDao)

