from backend.models.base_model import BaseModel
from backend.models.seller import Seller


name = 'Clara'
email = 'clara@olist.com'
phone = '(41) 9 3542-3456'
seller = Seller(name, phone, email)


def test_compare_column_model():
    assert seller.name == name
    assert seller.email == email
    assert seller.phone == phone


def test_compare_type_column_model():
    assert type(seller.name) == str
    assert type(seller.email) == str
    assert type(seller.phone) == str


def test_compare_isinstance():
    assert isinstance(seller, BaseModel)
    assert isinstance(seller, Seller)


def test_has_attribute():
    assert hasattr(seller, 'name')
    assert hasattr(seller, 'phone')
    assert hasattr(seller, 'email')


def test_validate_email():
    try:
        Seller('Test', '(41) 9 3542-3456', 'testolist.com')
    except Exception as e:
        assert isinstance(e, ValueError)


def test_validate_phone():
    try:
        Seller('Test', 'aaaaa', 'test@olist.com')
    except Exception as e:
        assert isinstance(e, ValueError)
