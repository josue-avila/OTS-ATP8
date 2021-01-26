from backend.models.base_model import BaseModel, Base


def test_base_model_instance():
    model = BaseModel()

    assert isinstance(model, BaseModel)
    assert issubclass(BaseModel, Base)
    assert model.__abstract__
    assert hasattr(model, 'id_')
