import sys

sys.path.append('.')

from backend.dao.marketplace_dao import *
from backend.controllers.log_controller import *


def save_marketplace(marketplace: Marketplace) -> None:
    if isinstance(marketplace.name, str) and isinstance(marketplace.description, str):
        save_marketplace_db(marketplace)

    create_log('set', 'save_marketplace')


def read_marketplaces() -> list:
    marketplaces = read_marketplace_db()

    create_log('get', 'read_marketplace')

    return marketplaces
