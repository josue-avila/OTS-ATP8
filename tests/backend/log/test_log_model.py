from backend.models.base_model import BaseModel
from backend.models.log import Log


def test_product_model_instance():
    operetion = 'set'
    description = 'Descricao'

    log_model = Log(operetion, description)

    assert isinstance(log_model, Log)
    assert isinstance(log_model, BaseModel)
    assert log_model.operation == operetion
    assert log_model.description == description
