from backend.dao.db.base_dao import BaseDao
from backend.models.seller import Seller


def test_base_dao_instance():
    class Test:
        pass

    base_dao = BaseDao(Test)

    assert isinstance(base_dao, BaseDao)
    assert base_dao._BaseDao__type_model is Test


def test_base_dao_read_all_should_return_list():
    dao = BaseDao(Seller)

    result = dao.read_all()

    assert isinstance(result, list)


def test_base_dao_save_should_save_to_db():
    dao = BaseDao(Seller)
    name = 'Test'
    phone = '99999999999'
    email = 'mail@mail.com'
    s = Seller(name, phone, email)

    dao.save(s)
    result = dao.read_all()[-1]

    assert result.name == name
    assert result.phone == phone
    assert result.email == email
