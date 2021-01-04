import sys
sys.path.append('backend/')

from flask import Flask, render_template, request, redirect
from backend import read_products, save_product, save_marketplaces, read_marketplaces

app = Flask(__name__)

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/create-product')
def form_product():
    products = read_products()
    return render_template('create_product.html', title = 'Produtos', list = products)

@app.route('/products', methods=["GET", "POST"])
def product_list():
    if request.method == 'POST':
        save_product(request.form)
    products = read_products()
    return render_template('product_list.html', title = 'Produtos', list = products)

@app.route('/marketplaces')
def list_marketplace():
    marketplaces = read_marketplaces()
    return render_template('marketplaces.html', title = 'Marketplaces',list = marketplaces)

@app.route('/new_marketplace')
def new_marketplace():
    return render_template('new_marketplace.html', title ='Novo Marketplace')

@app.route('/create_marketplace',methods=['POST'])
def create_markestplace():
    name = request.form.get("name")
    description = request.form.get("description")
    save_marketplaces(name,description)
    return redirect('/marketplaces')

app.run(debug=True)