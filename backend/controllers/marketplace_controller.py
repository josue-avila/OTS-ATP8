import sys
sys.path.append('.')

from backend.dao.marketplace_dao import *
from backend.controllers.log_controller import *

def save_marketplace(marketplace) -> None:
    if isinstance(marketplace.get('name'), str) and isinstance(marketplace.get('description'), str):
        save_marketplace_db(marketplace.get('name'), marketplace.get('description'))
    
    create_log('set', 'save_marketplace')

def read_marketplaces() -> list:
    sellers = read_marketplace_db()

    create_log('get', 'read_marketplace')

    return sellers