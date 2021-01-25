from backend.models.seller import Seller
from backend.controllers.seller_controller import SellerController

sellerController = SellerController()

name = 'Clara'
email = 'clara@olist.com'
phone = '(41) 9 3542-3456'
identifier = 942
seller = Seller(name, phone, email, identifier)

def test_compare_column_model_to_var():
    assert seller.name == name
    assert seller.email == email
    assert seller.phone == phone
    assert seller.id_ == identifier

def test_compare_type_column_model_to_str():
    assert type(seller.name) == str
    assert type(seller.email) == str
    assert type(seller.phone) == str
    assert type(seller.id_) == int
