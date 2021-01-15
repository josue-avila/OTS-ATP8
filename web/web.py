import sys

sys.path.append('.')
from flask import Flask, render_template, request, redirect, url_for
from backend.controllers.marketplace_controller import *
from backend.controllers.category_controller import *
from backend.controllers.seller_controller import *
from backend.controllers.log_controller import *
from backend.controllers.product_controller import *  # pylint: disable=import-error
from backend.models.category import Category
from backend.models.marketplace import Marketplace
from backend.models.product import Product
from backend.models.seller import Seller


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

marketplace_controller = MarketplaceController()
category_controller = CategoryController()
product_controller = ProductController()
seller_controller = SellerController()
log_controller = LogController()


@app.route('/')
def menu():
    return render_template('index.html')


# PRODUTOS
@app.route('/create_product')
def new_product():
    return render_template('create_product.html', title='Novo produto')


@app.route('/products', methods=["GET", "POST"])
def list_product():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        product = Product(name, description, price)
        product_controller.create(product)
    products = product_controller.read_all()
    return render_template('list_product.html', title='Products', list=products)


@app.route('/products/<int:id>', methods=['GET', 'POST'])
def edit_product(id: int):
    if request.method == "POST":
        name = request.form.get('name')
        desc = request.form.get('description')
        price = request.form.get('price')
        new_product = Product(name, desc, price, id)
        product_controller.update(new_product)
        return redirect(url_for('list_product'))
    product = product_controller.read_by_id(id)
    return render_template('edit_product.html', title='Product', object=product)


@app.route('/products/<int:id>/delete', methods=['GET'])
def erase_product(id: int):
    product_controller.delete(id)
    return redirect(url_for('list_product'))


# MARKETPLACES
@app.route('/marketplaces', methods=['GET', 'POST'])
def list_marketplace():
    if request.method == "POST":
        name = request.form.get('name')
        description = request.form.get('description')
        marketplace = Marketplace(name, description)
        marketplace_controller.create(marketplace)
    marketplaces = marketplace_controller.read_all()
    return render_template('list_marketplace.html', title='Marketplaces', list=marketplaces)


@app.route('/create_marketplace')
def new_marketplace():
    return render_template('create_marketplace.html', title='Novo Marketplace')


@app.route('/marketplaces/<int:id>', methods=['GET', 'POST'])
def edit_marketplace(id: int):
    if request.method == "POST":
        name = request.form.get('name')
        desc = request.form.get('description')
        new_marketplace = Marketplace(name, desc, id)
        marketplace_controller.update(new_marketplace)
        return redirect(url_for('list_marketplace'))
    marketplace = marketplace_controller.read_by_id(id)
    return render_template('edit_marketplace.html', title='Marketplace', object=marketplace)


@app.route('/marketplaces/<int:id>/delete', methods=['GET'])
def erase_marketplace(id: int):
    marketplace_controller.delete(id)
    return redirect(url_for('list_marketplace'))


# CATEGORIAS
@app.route('/create_category')
def new_category():
    return render_template('create_category.html', title='Nova Categoria')


@app.route('/categories', methods=['GET', 'POST'])
def list_category():
    if request.method == "POST":
        name = request.form.get('name')
        desc = request.form.get('description')
        category = Category(name, desc)
        category_controller.create(category)
    categories = category_controller.read_all()
    return render_template('list_category.html', title='Categories', list=categories)


@app.route('/categories/<int:id>', methods=['GET', 'POST'])
def edit_category(id: int):
    if request.method == "POST":
        name = request.form.get('name')
        desc = request.form.get('description')
        new_category = Category(name, desc, id)
        category_controller.update(new_category)
        return redirect(url_for('list_category'))
    category = category_controller.read_by_id(id)
    return render_template('edit_category.html', title='Category', object=category)


@app.route('/categories/<int:id>/delete', methods=['GET'])
def erase_category(id: int):
    category_controller.delete(id)
    return redirect(url_for('list_category'))


# SELLERS
@app.route('/create_seller')
def new_seller():
    return render_template('create_seller.html', title='Novo seller')


@app.route('/sellers', methods=["GET", "POST"])
def list_seller():
    if request.method == "POST":
        fullname = request.form.get('fullname')
        phone = request.form.get('phone')
        email = request.form.get('email')
        seller = Seller(fullname, phone, email)
        seller_controller.create(seller)
    sellers = seller_controller.read_all()
    return render_template('list_seller.html', title='Sellers', list=sellers)


@app.route('/sellers/<int:id>', methods=['GET', 'POST'])
def edit_seller(id: int):
    if request.method == "POST":
        fullname = request.form.get('fullname')
        phone = request.form.get('phone')
        email = request.form.get('email')
        new_seller = Seller(fullname, phone, email, id)
        seller_controller.update(new_seller)
        return redirect(url_for('list_seller'))
    seller = seller_controller.read_by_id(id)
    return render_template('edit_seller.html', title='Seller', object=seller)


@app.route('/sellers/<int:id>/delete', methods=['GET'])
def erase_seller(id: int):
    seller_controller.delete(id)
    return redirect(url_for('list_seller'))


# LOGS
@app.route('/logs', methods=["GET", "POST"])
def list_logs():
    logs = log_controller.read_all()
    return render_template('list_log.html', title='Logs', list=logs)


app.run(debug=True)
