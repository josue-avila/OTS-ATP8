from backend.models.base_model import BaseModel
from backend.models.marketplace import Marketplace


def test_marketplace_model_instance():
    name = 'Marketplace teste'
    description = 'Descrição teste'

    marketplace = Marketplace(name, description)

    assert isinstance(marketplace, BaseModel)
    assert isinstance(marketplace, Marketplace)
    assert marketplace.name == name
    assert marketplace.description == description

