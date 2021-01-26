from backend.controllers.base_controller import BaseController
from backend.dao.db.base_dao import BaseDao
from backend.models.seller import Seller


def test_base_controller_instance():
    class Test:
        pass

    domain_name = 'Domain'
    base_dao = BaseDao(Test)
    base_controller = BaseController(base_dao, domain_name)

    assert isinstance(base_controller, BaseController)
    assert base_controller._BaseController__domain_name is domain_name
    assert base_controller._BaseController__dao is base_dao


def test_controller_read_all_should_return_list():
    domain_name = 'Seller'
    base_dao = BaseDao(Seller)
    controller = BaseController(base_dao, domain_name)

    result = controller.read_all()

    assert isinstance(result, list)


def test_base_controller_create_should_save_to_db():
    domain_name = 'Seller'
    base_dao = BaseDao(Seller)
    controller = BaseController(base_dao, domain_name)

    name = 'Test'
    phone = '99999999999'
    email = 'mail@mail.com'
    s = Seller(name, phone, email)

    controller.create(s)
    result = controller.read_all()[-1]

    assert result.name == name
    assert result.phone == phone
    assert result.email == email
