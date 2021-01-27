from backend.models.base_model import BaseModel
from backend.models.product import Product

name = 'Test'
description = 'description'
price = 350

product = Product(name, description, price)


def test_compare_column_model():
    assert product.name == name
    assert product.description == description


def test_compare_type_column_model():
    assert type(product.name) == str
    assert type(product.description) == str
    assert type(product.price) == float


def test_compare_isinstance():
    assert isinstance(product, BaseModel)
    assert isinstance(product, Product)


def test_has_attribute():
    assert hasattr(product, 'name')
    assert hasattr(product, 'description')
    assert hasattr(product, 'price')
