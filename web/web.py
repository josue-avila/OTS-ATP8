from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/products')
def create_product():
    return 0

@app.route('/marketplaces')
def create_mktplace():
    return render_template('marketplaces.html')