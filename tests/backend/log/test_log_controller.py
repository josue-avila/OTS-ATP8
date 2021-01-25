from backend.controllers.log_controller import LogController


def test_log_controller_instance():
    log_controller = LogController()
    assert isinstance(log_controller, LogController)
