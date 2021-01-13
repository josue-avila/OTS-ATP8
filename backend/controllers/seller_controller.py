import sys
sys.path.append('.')

from backend.dao.seller_dao import *
from backend.controllers.log_controller import *

def save_seller(seller: Seller) -> None:
    if isinstance(seller.fullname, str) and isinstance(seller.phone, str) and isinstance(seller.email, str):
        save_seller_db(seller)

    create_log('set', 'seller')

def read_sellers() -> list:
    sellers = read_sellers_db()
    create_log('get', 'sellers')

    return sellers