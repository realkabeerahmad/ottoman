from flask import Blueprint, render_template
from app.models.product import Product, Category

main = Blueprint('main', __name__)

@main.route('/')
def index():
    featured_products = Product.query.filter_by(is_featured=True, status='active').limit(6).all()
    featured_categories = Category.query.filter_by(is_featured=True, status='active').all()
    return render_template('main/index.html',
                           products=featured_products,
                           featured_categories=featured_categories)

@main.route('/about')
def about():
    return render_template('main/about.html')

@main.route('/contact')
def contact():
    return render_template('main/contact.html')
