from backend.models.base_model import BaseModel
from backend.models.category import Category

name = 'Category'
description = 'Description'

category = Category(name, description)


def test_compare_column_model():
    assert category.name == name
    assert category.description == description


def test_compare_type_column_model():
    assert type(category.name) == str
    assert type(category.description) == str


def test_compare_isinstance():
    assert isinstance(category, BaseModel)
    assert isinstance(category, Category)


def test_has_attribute():
    assert hasattr(category, 'name')
    assert hasattr(category, 'description')
