import os
from app import create_app, db
from app.models.user import User
from app.models.product import Category, Product, ProductVariant
from app.models.order import Order, OrderItem, ShippingMethod, PaymentMethod, OrderStatus, Coupon
from app.models.cart import Cart, CartItem

app = create_app(os.getenv('FLASK_ENV') or 'default')

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Category': Category,
        'Product': Product,
        'ProductVariant': ProductVariant,
        'Order': Order,
        'OrderItem': OrderItem,
        'ShippingMethod': ShippingMethod,
        'PaymentMethod': PaymentMethod,
        'OrderStatus': OrderStatus,
        'Coupon': Coupon,
        'Cart': Cart,
        'CartItem': CartItem
    }

if __name__ == '__main__':
    app.run(debug=True)
