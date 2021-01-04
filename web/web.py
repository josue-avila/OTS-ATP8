import sys
sys.path.append('backend/')

from flask import Flask, render_template, request, redirect

from backend import read_products,save_marketplaces


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
def list_marketplace():
    return render_template('marketplaces.html', title = 'Marketplaces')

@app.route('/new_marketplace')
def new_marketplace():
    return render_template('new_marketplace.html', title ='Novo Marketplace')

@app.route('/create_marketplace',methods=['POST'])
def create_markestplace():
    name = request.form.get("name")
    description = request.form.get("description")
    save_marketplaces(name,description)
    return redirect('/')

app.run(debug=True)