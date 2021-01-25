from backend.models.base_model import BaseModel
from backend.models.product import Product


def test_product_model_instance():
    name = 'Test'
    description = 'description'
    price = 350

    product = Product(name, description, price)

    assert isinstance(product, BaseModel)
    assert isinstance(product, Product)
    assert product.name == name
    assert product.description == description
    assert product.price == price
