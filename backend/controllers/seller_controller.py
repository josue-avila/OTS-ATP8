from backend.dao.db.seller_dao import save_seller_db, read_sellers_db
from backend.controllers.log_controller import save_log
from backend.models.seller import Seller


def save_seller(seller: Seller) -> None:
    if isinstance(seller.fullname, str) and isinstance(seller.phone, str) and isinstance(seller.email, str):
        save_seller_db(seller)

    save_log('set', 'seller')

def read_sellers() -> list:
    sellers = read_sellers_db()
    save_log('get', 'sellers')

    return sellers