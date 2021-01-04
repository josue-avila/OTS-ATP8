from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/products')
def create_product():
    return render_template('product_list.html', title = 'Produtos')

@app.route('/marketplaces')
def create_marketplace():
    return render_template('marketplaces.html', title = 'Marketplaces')

app.run(debug=True)