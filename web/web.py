from flask import Flask, render_template, request
import sys

sys.path.append('backend')
from backend import read_products

app = Flask(__name__)

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/create-product')
def create_product():
    products = read_products()
    return render_template('create_product.html', title = 'Produtos', list = products)

@app.route('/products')
def product_list():
    # se método post
        # chamar função de criar produto
    products = read_products()
    return render_template('product_list.html', title = 'Produtos', list = products)

@app.route('/marketplaces')
def create_marketplace():
    return render_template('marketplaces.html', title = 'Marketplaces')

app.run(debug=True)