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

@app.route('/marketplaces',methods=['GET','POST'])
def list_marketplace():
    if request.method == 'POST':
        save_marketplaces(request.form)
    marketplaces = read_marketplaces()
    return render_template('marketplaces_list.html', title = 'Marketplaces',list = marketplaces)

@app.route('/create_marketplace')
def new_marketplace():
    return render_template('create_marketplace.html', title ='Novo Marketplace')


app.run(debug=True)