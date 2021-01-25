from flask import Blueprint, render_template, request, redirect, url_for

from backend.controllers.seller_controller import SellerController
from backend.models.seller import Seller

sellers = Blueprint('seller', __name__)

seller_controller = SellerController()


@sellers.route('/create_seller')
def new_seller():
    return render_template('create_seller.html', title='Novo seller')


@sellers.route('/sellers', methods=["GET", "POST"])
def list_seller():
    if request.method == "POST":
        fullname = request.form.get('fullname')
        phone = request.form.get('phone')
        email = request.form.get('email')
        seller = Seller(fullname, phone, email)
        seller_controller.create(seller)
    sellers = seller_controller.read_all()
    return render_template('list_seller.html', title='Sellers', list=sellers)


@sellers.route('/sellers/<int:id>', methods=['GET', 'POST'])
def edit_seller(id: int):
    if request.method == "POST":
        fullname = request.form.get('fullname')
        phone = request.form.get('phone')
        email = request.form.get('email')
        new_seller = Seller(fullname, phone, email, id)
        seller_controller.update(new_seller)
        return redirect('/sellers')
    seller = seller_controller.read_by_id(id)
    return render_template('edit_seller.html', title='Seller', object=seller)


@sellers.route('/sellers/<int:id>/delete', methods=['GET'])
def erase_seller(id: int):
    seller_controller.delete(id)
    return redirect(url_for('list_seller'))
