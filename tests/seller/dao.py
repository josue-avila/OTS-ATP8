from backend.dao.db.base_dao import BaseDao
from backend.dao.db.seller_dao import SellerDao

seller_dao = SellerDao()

assert isinstance(seller_dao, BaseDao)