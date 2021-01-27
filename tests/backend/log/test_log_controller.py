from backend.controllers.log_controller import LogController
from backend.models.log import Log

log = Log('teste', 'test')
log_controller = LogController()


def test_log_controller_instance():
    assert isinstance(log_controller, LogController)


def test_method_save_log_should_return_primary_key():
    result = log_controller.save(log)
    assert isinstance(result, int)


def tes_method_readall_must_return_list():
    assert isinstance(log_controller.read_all() ,list)


