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


def test_base_dao_save_should_create_to_db():
    dao = BaseDao(Seller)
    name = 'Test'
    phone = '99999999999'
    email = 'mail@mail.com'
    s = Seller(name, phone, email)

    id_aux = dao.save(s)
    result = dao.read_by_id(id_aux)

    assert id_aux == result.id_
    assert result.name == name
    assert result.phone == phone
    assert result.email == email
    assert isinstance(result.name, str)
    assert isinstance(result.phone, str)
    assert isinstance(result.email, str)


def test_base_dao_delete_should_delete_in_db():
    dao = BaseDao(Seller)
    name = 'Test1'
    phone = '111111111111'
    email = 'mail1@mail.com'
    s = Seller(name, phone, email)

    id_aux = dao.save(s)
    seller_aux = dao.read_by_id(id_aux)

    dao.delete(seller_aux)

    result = dao.read_by_id(id_aux)

    assert result is None


def test_base_dao_save_should_update_in_db():
    dao = BaseDao(Seller)
    name = 'Test2'
    phone = '2222222222'
    email = 'mail2@mail.com'
    s = Seller(name, phone, email)

    id_aux = dao.save(s)

    s.id_ = id_aux
    s.name = 'Test3'
    s.phone = '333333333333'
    s.email = 'mail3@mail.com'

    id_updated = dao.save(s)

    seller_db = dao.read_by_id(id_updated)

    assert seller_db.id_ == s.id_
    assert seller_db.name == s.name
    assert seller_db.phone == s.phone
    assert seller_db.email == s.email


def test_base_dao_read_by_id_should_return_model():
    dao = BaseDao(Seller)
    name = 'Test4'
    phone = '444444444444'
    email = 'mail4@mail.com'
    s = Seller(name, phone, email)

    id_aux = dao.save(s)

    result = dao.read_by_id(id_aux)

    assert isinstance(result, Seller)
