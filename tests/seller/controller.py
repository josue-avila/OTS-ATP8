from backend.controllers.base_controller import BaseController
from backend.controllers.seller_controller import SellerController
from backend.models.seller import Seller

seller_controller = SellerController()
seller = Seller('clara', '(53) 0 4254-4324', 'clara@olist.com')

def test_method_seller_should_return_none():
    assert seller_controller.create(seller) == None
    assert seller_controller.delete(1) == None

def test_read_sellers_should_return_list():
    assert isinstance(seller_controller.read_all(), list)

def test_compare_instance_seller_controller_to_basecontroller():
    assert isinstance(seller_controller, BaseController)