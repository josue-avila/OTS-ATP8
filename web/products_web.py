from flask import Blueprint, render_template, request, redirect, url_for

from backend.controllers.product_controller import ProductController
from backend.models.product import Product

products = Blueprint('product', __name__)

product_controller = ProductController()


@products.route('/create_product')
def new_product():
    return render_template('create_product.html', title='Novo produto')


@products.route('/products', methods=["GET", "POST"])
def list_product():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        product = Product(name, description, price)
        product_controller.create(product)
    products = product_controller.read_all()
    return render_template('list_product.html', title='Products', list=products)


@products.route('/products/<int:id>', methods=['GET', 'POST'])
def edit_product(id: int):
    if request.method == "POST":
        name = request.form.get('name')
        desc = request.form.get('description')
        price = request.form.get('price')
        new_product = Product(name, desc, price, id)
        product_controller.update(new_product)
        return redirect('/products')
    product = product_controller.read_by_id(id)
    return render_template('edit_product.html', title='Product', object=product)


@products.route('/products/<int:id>/delete', methods=['GET'])
def erase_product(id: int):
    product_controller.delete(id)
    return redirect(url_for('list_product'))
