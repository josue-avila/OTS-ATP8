from backend.controllers.base_controller import BaseController
from backend.controllers.category_controller import CategoryController


def test_category_controller_instance():
    category_controller = CategoryController()

    assert isinstance(category_controller, BaseController)
    assert isinstance(category_controller, CategoryController)
