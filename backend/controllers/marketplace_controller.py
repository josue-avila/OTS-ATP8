from backend.dao.db.marketplace_dao import read_marketplaces_db, save_marketplace_db
from backend.controllers.log_controller import save_log
from backend.models.marketplace import Marketplace


def save_marketplace(marketplace: Marketplace) -> None:
    if isinstance(marketplace.name, str) and isinstance(marketplace.description, str):
        save_marketplace_db(marketplace)

    save_log('set', 'marketplace')


def read_marketplaces() -> list:
    marketplaces = read_marketplaces_db()

    save_log('get', 'marketplaces')

    return marketplaces
