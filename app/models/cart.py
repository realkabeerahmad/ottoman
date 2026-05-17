from datetime import datetime
import uuid
from app import db

class Cart(db.Model):
    __tablename__ = 'carts'
    
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(128), unique=True, index=True) # For guest users
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=True) # For logged in users
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    items = db.relationship('CartItem', backref='cart', lazy='dynamic', cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Cart {self.id}>'
        
    @property
    def total_items(self):
        return sum(item.quantity for item in self.items)
        
    @property
    def subtotal(self):
        return sum(item.effective_price * item.quantity for item in self.items if item.product)

class CartItem(db.Model):
    __tablename__ = 'cart_items'
    
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'), nullable=False)
    
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    variant_id = db.Column(db.Integer, db.ForeignKey('product_variants.id'), nullable=True)
    
    quantity = db.Column(db.Integer, default=1, nullable=False)
    
    added_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    product = db.relationship('Product')
    variant = db.relationship('ProductVariant')

    @property
    def effective_price(self):
        """Use variant price_override if set, else discount_price if set, else base price."""
        if self.variant and self.variant.price_override and self.variant.price_override > 0:
            return self.variant.price_override
        if not self.product:
            return 0
        if self.product.discount_price and self.product.discount_price > 0:
            return self.product.discount_price
        return self.product.price

    @property
    def line_total(self):
        return self.effective_price * self.quantity

    def __repr__(self):
        return f'<CartItem {self.product_id} qty {self.quantity}>'
