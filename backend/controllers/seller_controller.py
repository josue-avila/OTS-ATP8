import sys
sys.path.append('.')

from backend.dao.seller_dao import *
from backend.controllers.log_controller import *

def save_seller(seller) -> None:
    if isinstance(seller.get('fullname'), str) and isinstance(seller.get('phone'), str) and isinstance(seller.get('email'), str):
        save_seller_db(seller.get('fullname'), seller.get('phone'), seller.get('email'))

    create_log('set', 'save_sellers')

def read_sellers() -> list:
    sellers = read_sellers_db()
    create_log('get', 'read_sellers')

    return sellers