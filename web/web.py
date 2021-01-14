import sys
sys.path.append('.')
from flask import Flask, render_template, request, redirect, url_for
from backend.controllers.marketplace_controller import *
from backend.controllers.category_controller import *
from backend.controllers.seller_controller import *
from backend.controllers.log_controller import *
from backend.controllers.product_controller import *  # pylint: disable=import-error


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


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
        save_product(product)
    products = read_products()
    return render_template('list_product.html', title='Products', list=products)


@app.route('/products/<int:id>', methods=['GET', 'POST'])
def edit_product(id: int):
    if request.method == "POST":
        name = request.form.get('name')
        desc = request.form.get('description')
        price = request.form.get('price')
        new_product = Product(name, desc, price, id)
        update_product(new_product)
        return redirect(url_for('list_product'))
    product = read_product(id)
    return render_template('edit_product.html', title='Product', object=product)


# MARKETPLACES
@app.route('/marketplaces', methods=['GET', 'POST'])
def list_marketplace():
    if request.method == "POST":
        name = request.form.get('name')
        description = request.form.get('description')
        marketplace = Marketplace(name, description)
        save_marketplace(marketplace)
    marketplaces = read_marketplaces()
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
        update_marketplace(new_marketplace)
        return redirect(url_for('list_marketplace'))
    marketplace = read_marketplace(id)
    return render_template('edit_marketplace.html', title='Marketplace', object=marketplace)


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
        save_category(category)
    categories = read_categories()
    return render_template('list_category.html', title='Categories', list=categories)


@app.route('/categories/<int:id>', methods=['GET', 'POST'])
def edit_category(id: int):
    if request.method == "POST":
        name = request.form.get('name')
        desc = request.form.get('description')
        new_category = Category(name, desc, id)
        update_category(new_category)
        return redirect(url_for('list_category'))
    category = read_category(id)
    return render_template('edit_category.html', title='Category', object=category)


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
        save_seller(seller)
    sellers = read_sellers()
    return render_template('list_seller.html', title='Sellers', list=sellers)


@app.route('/sellers/<int:id>', methods=['GET', 'POST'])
def edit_seller(id: int):
    if request.method == "POST":
        fullname = request.form.get('fullname')
        phone = request.form.get('phone')
        email = request.form.get('email')
        new_seller = Seller(fullname, phone, email, id)
        update_seller(new_seller)
        return redirect(url_for('list_seller'))
    seller = read_seller(id)
    return render_template('edit_seller.html', title='Seller', object=seller)


# LOGS
@app.route('/logs', methods=["GET", "POST"])
def list_logs():
    return render_template('list_log.html', title='Logs', list=read_logs())


app.run(debug=True)
