from backend.models.base_model import BaseModel
from backend.models.category import Category


def test_category_model_instance():
    name = 'Category'
    description = 'Description'

    category = Category(name, description)

    assert isinstance(category, BaseModel)
    assert isinstance(category, Category)
    assert category.name == name
    assert category.description == description
