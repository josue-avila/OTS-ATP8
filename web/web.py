import sys
sys.path.append('backend/')

from flask import Flask, render_template, request, redirect
from backend import read_products, save_product, save_marketplaces, read_marketplaces, search_mktplace #pylint: disable=import-error
from category import add_new_category #pylint: disable=import-error
from seller import save_seller,read_sellers #pylint: disable=import-error

app = Flask(__name__)

@app.route('/')
def menu():
    return render_template('index.html')

@app.route('/create-product')
def form_product():
    products = read_products()
    return render_template('create_product.html', title = 'Produtos', list = products)

@app.route('/products', methods=["GET", "POST"])
def product_list():
    save = 'false'
    if request.method == 'POST':
        save_product(request.form)
        save = 'true'
    products = read_products()
    return render_template('product_list.html', title = 'Produtos', list = products, save = save)

@app.route('/marketplaces',methods=['GET','POST'])
def list_marketplace():
    save = 'false'
    if request.method == 'POST':
        search_mktplace(request.form)
        save = 'true'
    marketplaces = read_marketplaces()
    return render_template('marketplaces_list.html', title = 'Marketplaces',list = marketplaces, save = save)

@app.route('/create_marketplace')
def new_marketplace():
    return render_template('create_marketplace.html', title ='Novo Marketplace')


@app.route('/create_category')
def new_category():
    return render_template('create_category.html', title ='Nova Categoria')

@app.route('/categories',methods=['GET','POST'])
def list_categories():
   
    cat = request.form.get('name')
    cat_desc = request.form.get('description')

    print(cat)
    print(cat_desc)
    if cat != None:
        add_new_category(cat, cat_desc)
    #lista vazia apenas para manter o padrão! Será necessário implementar a função de listagem das categorias futuramente
    categories = []
    return render_template('categories_list.html', title = 'Categories',list = categories)
    
@app.route('/create-seller')
def form_seller():
    return render_template('create_seller.html', title = 'Sellers')

@app.route('/sellers', methods=["GET", "POST"])
def seller_list():
    save = 'false'
    if request.method == 'POST':
        save_seller(request.form, "backend/db/sellers.txt")
        save = 'true'
    sellers = read_sellers()
    return render_template('seller_list.html', title = 'Sellers', list = sellers, save = save)

app.run(debug=True)