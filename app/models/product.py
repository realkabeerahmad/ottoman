from datetime import datetime
from app import db

class Category(db.Model):
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    slug = db.Column(db.String(64), unique=True, nullable=False, index=True)
    description = db.Column(db.Text)
    featured_image = db.Column(db.String(255))
    parent_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    is_featured = db.Column(db.Boolean, default=False)
    status = db.Column(db.String(20), default='active')
    
    subcategories = db.relationship('Category', backref=db.backref('parent', remote_side=[id]))
    products = db.relationship('Product', backref='category', lazy='dynamic')

    def __repr__(self):
        return f'<Category {self.name}>'

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    slug = db.Column(db.String(128), unique=True, index=True, nullable=False)
    short_description = db.Column(db.String(255))
    description = db.Column(db.Text)
    sku = db.Column(db.String(64), unique=True, index=True)
    brand = db.Column(db.String(64), default='Ottoman Time')
    
    main_image = db.Column(db.String(255))
    # We could use JSON for gallery but for sqlite compatibility, maybe comma-separated or separate table
    # We will use a separate table for gallery images if needed, or simple string for now
    
    price = db.Column(db.Float, nullable=False)
    discount_price = db.Column(db.Float)
    
    stock_status = db.Column(db.String(20), default='in_stock') # in_stock, out_of_stock, pre_order
    quantity = db.Column(db.Integer, default=0) # Total stock quantity available
    is_featured = db.Column(db.Boolean, default=False)
    status = db.Column(db.String(20), default='active') # active, inactive
    
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    variants = db.relationship('ProductVariant', backref='product', lazy='dynamic', cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Product {self.name}>'

    @property
    def total_quantity(self):
        if self.variants.count() > 0:
            return sum(v.quantity for v in self.variants)
        return self.quantity

    @property
    def is_in_stock(self):
        if self.stock_status == 'out_of_stock':
            return False
        return self.total_quantity > 0

class ProductVariant(db.Model):
    __tablename__ = 'product_variants'
    
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    
    sku = db.Column(db.String(64), unique=True, index=True)
    color = db.Column(db.String(64))
    strap_type = db.Column(db.String(64))
    size = db.Column(db.String(64))
    edition = db.Column(db.String(64))
    
    price_override = db.Column(db.Float) # If the variant has a different price
    quantity = db.Column(db.Integer, default=0)
    image = db.Column(db.String(255))
    
    def __repr__(self):
        return f'<ProductVariant {self.sku}>'
