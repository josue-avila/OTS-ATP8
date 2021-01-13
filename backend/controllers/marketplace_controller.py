from backend.dao.db.marketplace_dao import read_marketplaces_db, save_marketplace_db, read_marketplace_db, update_marketplace_db
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


def read_marketplace(id: int) -> Marketplace:
    marketplace = read_marketplace_db(id)
    save_log('read', 'marketplace')
    return marketplace


def update_marketplace(marketplace: Marketplace) -> None:
    new_marketplace = read_marketplace(marketplace.id)
    new_marketplace.name = marketplace.name
    new_marketplace.description = marketplace.description
    update_marketplace_db(new_marketplace)
    save_log('update', 'marketplace')
