from flask import Blueprint, render_template, request, redirect, url_for

from backend.controllers.category_controller import CategoryController
from backend.models.category import Category

categories = Blueprint('category', __name__)

category_controller = CategoryController()


@categories.route('/create_category')
def new_category():
    return render_template('create_category.html', title='Nova Categoria')


@categories.route('/categories', methods=['GET', 'POST'])
def list_category():
    if request.method == "POST":
        name = request.form.get('name')
        desc = request.form.get('description')
        category = Category(name, desc)
        category_controller.create(category)
    categories = category_controller.read_all()
    return render_template('list_category.html', title='Categories', list=categories)


@categories.route('/categories/<int:id>', methods=['GET', 'POST'])
def edit_category(id: int):
    if request.method == "POST":
        name = request.form.get('name')
        desc = request.form.get('description')
        new_category = Category(name, desc, id)
        category_controller.update(new_category)
        return redirect(url_for('list_category'))
    category = category_controller.read_by_id(id)
    return render_template('edit_category.html', title='Category', object=category)


@categories.route('/categories/<int:id>/delete', methods=['GET'])
def erase_category(id: int):
    category_controller.delete(id)
    return redirect(url_for('list_category'))
