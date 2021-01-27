from backend.models.base_model import BaseModel
from backend.models.marketplace import Marketplace

name = 'Marketplace teste'
description = 'Descrição teste'

marketplace = Marketplace(name, description)


def test_compare_column_model():
    assert marketplace.name == name
    assert marketplace.description == description


def test_compare_type_column_model():
    assert type(marketplace.name) == str
    assert type(marketplace.description) == str


def test_compare_isinstance():
    assert isinstance(marketplace, BaseModel)
    assert isinstance(marketplace, Marketplace)


def test_has_attribute():
    assert hasattr(marketplace, 'name')
    assert hasattr(marketplace, 'description')

