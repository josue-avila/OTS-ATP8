import sys
sys.path.append('.')
from flask import Flask, render_template, request, redirect
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
@app.route('/create-product')
def form_product():
    products = read_products()
    return render_template('create_product.html', title='Produtos', list=products)


@app.route('/products', methods=["GET", "POST"])
def product_list():
    save = 'false'
    if request.method == 'POST':
        save_product(request.form)
        save = 'true'
    products = read_products()
    return render_template('product_list.html', title='Produtos', list=products, save=save)


# MARKETPLACES
@app.route('/marketplaces', methods=['GET', 'POST'])
def list_marketplace():
    save = 'false'
    if request.method == 'POST':
        save_marketplace(request.form)
        save = 'true'
    marketplaces = read_marketplaces()
    return render_template('marketplaces_list.html', title='Marketplaces', list=marketplaces, save=save)


@app.route('/create_marketplace')
def new_marketplace():
    return render_template('create_marketplace.html', title='Novo Marketplace')


# CATEGORIAS
@app.route('/create_category')
def new_category():
    return render_template('create_category.html', title='Nova Categoria')


@app.route('/categories', methods=['GET', 'POST'])
def list_categories():

    cat = request.form.get('name')
    cat_desc = request.form.get('description')
    if cat != None:
        add_new_category(cat, cat_desc)
        #search_category(cat, cat_desc)
    categories = read_categories()
    return render_template('categories_list.html', title='Categories', list=categories)


# SELLERS
@app.route('/create-seller')
def form_seller():
    return render_template('create_seller.html', title='Sellers')


@app.route('/sellers', methods=["GET", "POST"])
def seller_list():
    save = 'false'
    if request.method == 'POST':
        save_seller(request.form)
        save = 'true'
    sellers = read_sellers()
    return render_template('seller_list.html', title='Sellers', list=sellers, save=save)


# LOGS
@app.route('/logs', methods=["GET", "POST"])
def logs_list():
    return render_template('logs_list.html', title='Logs', list=read_logs())


app.run(debug=True)
