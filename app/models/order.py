from datetime import datetime
import uuid
from app import db

class ShippingMethod(db.Model):
    __tablename__ = 'shipping_methods'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    cost = db.Column(db.Float, nullable=False, default=0.0)
    delivery_estimate = db.Column(db.String(64))
    is_active = db.Column(db.Boolean, default=True)

class PaymentMethod(db.Model):
    __tablename__ = 'payment_methods'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False) # e.g. "Cash on Delivery", "Bank Transfer"
    instructions = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True)

class OrderStatus(db.Model):
    __tablename__ = 'order_statuses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
    description = db.Column(db.Text)
    is_default = db.Column(db.Boolean, default=False)
    is_system = db.Column(db.Boolean, default=False)  # System statuses cannot be deleted/renamed

    # Default system statuses seeded on first run
    SYSTEM_STATUSES = [
        {'name': 'Pending',    'description': 'Order received, awaiting confirmation', 'is_default': True},
        {'name': 'Confirmed',  'description': 'Order confirmed by the house'},
        {'name': 'Processing', 'description': 'Order is being prepared'},
        {'name': 'Shipped',    'description': 'Order dispatched to courier'},
        {'name': 'Delivered',  'description': 'Order delivered to recipient'},
        {'name': 'Cancelled',  'description': 'Order cancelled'},
        {'name': 'Refunded',   'description': 'Payment refunded to customer'},
    ]

    @classmethod
    def seed_defaults(cls, db_session):
        """Insert system statuses if they don't exist yet."""
        for status_data in cls.SYSTEM_STATUSES:
            existing = cls.query.filter_by(name=status_data['name']).first()
            if not existing:
                s = cls(
                    name=status_data['name'],
                    description=status_data.get('description', ''),
                    is_default=status_data.get('is_default', False),
                    is_system=True
                )
                db_session.add(s)
        db_session.commit()
    
class Coupon(db.Model):
    __tablename__ = 'coupons'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(64), unique=True, index=True, nullable=False)
    discount_type = db.Column(db.String(20), default='percentage') # percentage or fixed
    discount_value = db.Column(db.Float, nullable=False)
    valid_from = db.Column(db.DateTime, default=datetime.utcnow)
    valid_until = db.Column(db.DateTime, nullable=True)
    usage_limit = db.Column(db.Integer, nullable=True)
    times_used = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)

class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    order_number = db.Column(db.String(64), unique=True, index=True, default=lambda: str(uuid.uuid4()).split('-')[0].upper())
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True) # Nullable for guest checkout
    
    # Customer Details
    customer_email = db.Column(db.String(120), nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_phone = db.Column(db.String(20))
    
    # Shipping Details
    shipping_address = db.Column(db.Text, nullable=False)
    shipping_city = db.Column(db.String(64), nullable=False)
    shipping_postal_code = db.Column(db.String(20))
    shipping_country = db.Column(db.String(64), default='Pakistan')
    
    # Pricing Breakdown
    subtotal = db.Column(db.Float, nullable=False)
    tax_amount = db.Column(db.Float, default=0.0)
    shipping_cost = db.Column(db.Float, default=0.0)
    discount_amount = db.Column(db.Float, default=0.0)
    total_amount = db.Column(db.Float, nullable=False)
    
    # Methods & Status
    shipping_method_id = db.Column(db.Integer, db.ForeignKey('shipping_methods.id'))
    payment_method_id = db.Column(db.Integer, db.ForeignKey('payment_methods.id'))
    order_status_id = db.Column(db.Integer, db.ForeignKey('order_statuses.id'), nullable=True)
    coupon_id = db.Column(db.Integer, db.ForeignKey('coupons.id'), nullable=True)
    
    payment_status = db.Column(db.String(20), default='pending') # pending, paid, failed, refunded
    # Legacy string status fallback
    status_string = db.Column(db.String(64), default='Pending')
    
    tracking_number = db.Column(db.String(64))
    notes = db.Column(db.Text)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    items = db.relationship('OrderItem', backref='order', lazy='dynamic', cascade="all, delete-orphan")
    shipping_method = db.relationship('ShippingMethod')
    payment_method = db.relationship('PaymentMethod')
    status = db.relationship('OrderStatus')
    coupon = db.relationship('Coupon')

    def __repr__(self):
        return f'<Order {self.order_number}>'

class OrderItem(db.Model):
    __tablename__ = 'order_items'
    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    variant_id = db.Column(db.Integer, db.ForeignKey('product_variants.id'), nullable=True)
    
    product_name = db.Column(db.String(128))
    sku = db.Column(db.String(64))
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    
    def __repr__(self):
        return f'<OrderItem {self.product_name} x {self.quantity}>'
