from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/products')
def create_product():
    return render_template('product_list.html', title = 'Produtos')

app.run(debug=True)