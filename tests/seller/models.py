from backend.models.seller import Seller
from backend.controllers.seller_controller import SellerController

sellerController = SellerController()

name = 'Clara'
email = 'clara@olist.com'
phone = '(41) 9 3542-3456'
identifier = 942
seller = Seller(name, phone, email, identifier)

def test_compare_name_model_to_var():
    assert seller.name == name

def test_compare_email_model_to_var():
    assert seller.email == email

def test_compare_phone_model_to_var():
    assert seller.phone == phone

def test_compare_id_model_to_var():
    assert seller.id_ == identifier

def test_compare_type_name_model_to_str():
    assert type(seller.name) == str

def test_compare_type_email_model_to_str():
    assert type(seller.email) == str

def test_compare_type_id_model_to_int():
    assert type(seller.id_) == int