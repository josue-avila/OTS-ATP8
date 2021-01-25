from backend.controllers.base_controller import BaseController
from backend.controllers.marketplace_controller import MarketplaceController


def test_marketplace_controller_instance():
    marketplace_controller = MarketplaceController()

    assert isinstance(marketplace_controller, BaseController)
    assert isinstance(marketplace_controller, MarketplaceController)

# test_marketplace_controller_instance()
