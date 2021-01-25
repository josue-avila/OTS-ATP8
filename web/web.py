from flask import Flask, render_template

from web.categories_web import categories
from web.logs_web import logs
from web.marketplaces_web import marketplaces
from web.products_web import products
from web.sellers_web import sellers

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

app.register_blueprint(products)
app.register_blueprint(marketplaces)
app.register_blueprint(categories)
app.register_blueprint(sellers)
app.register_blueprint(logs)


@app.route('/')
def menu():
    return render_template('index.html')
