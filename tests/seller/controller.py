from backend.controllers.base_controller import BaseController
from backend.controllers.seller_controller import SellerController
from backend.models.seller import Seller

seller_controller = SellerController()
seller = Seller('clara', '(53) 0 4254-4324', 'clara@olist.com')

assert seller_controller.create(seller) == None
assert isinstance(seller_controller.read_all(), list)
assert seller_controller.delete(1) == None
assert isinstance(seller_controller, BaseController)