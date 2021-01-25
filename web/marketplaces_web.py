from flask import Blueprint, render_template, request, redirect, url_for

from backend.controllers.marketplace_controller import MarketplaceController
from backend.models.marketplace import Marketplace

marketplaces = Blueprint('marketplace', __name__)

marketplace_controller = MarketplaceController()


@marketplaces.route('/marketplaces', methods=['GET', 'POST'])
def list_marketplace():
    if request.method == "POST":
        name = request.form.get('name')
        description = request.form.get('description')
        marketplace = Marketplace(name, description)
        marketplace_controller.create(marketplace)
    marketplaces = marketplace_controller.read_all()
    return render_template('list_marketplace.html', title='Marketplaces', list=marketplaces)


@marketplaces.route('/create_marketplace')
def new_marketplace():
    return render_template('create_marketplace.html', title='Novo Marketplace')


@marketplaces.route('/marketplaces/<int:id>', methods=['GET', 'POST'])
def edit_marketplace(id: int):
    if request.method == "POST":
        marketplace_update = marketplace_controller.read_by_id(id)
        name = request.form.get('name')
        desc = request.form.get('description')
        marketplace_update.name = name
        marketplace_update.description = desc
        marketplace_controller.update(marketplace_update)
        return redirect('/marketplaces')
    marketplace = marketplace_controller.read_by_id(id)
    return render_template('edit_marketplace.html', title='Marketplace', object=marketplace)


@marketplaces.route('/marketplaces/<int:id>/delete', methods=['GET'])
def erase_marketplace(id: int):
    marketplace_controller.delete(id)
    return redirect('/marketplaces')
