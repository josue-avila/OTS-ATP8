from backend.controllers.base_controller import BaseController
from backend.controllers.product_controller import ProductController


def test_product_controller_instance():
    product_controller = ProductController()

    assert isinstance(product_controller, BaseController)
    assert isinstance(product_controller, ProductController)
