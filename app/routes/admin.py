from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from app.models.order import Order, OrderItem, OrderStatus, ShippingMethod, PaymentMethod, Coupon
from app.models.product import Product, Category, ProductVariant
from app import db
import string
import random
import os
import uuid as uuid_lib
import cloudinary
import cloudinary.uploader

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_product_image(file):
    """Save an uploaded image to Cloudinary and return the secure URL."""
    if file and file.filename and allowed_file(file.filename):
        try:
            upload_result = cloudinary.uploader.upload(file)
            return upload_result.get('secure_url')
        except Exception as e:
            current_app.logger.error(f"Cloudinary upload failed: {str(e)}")
            return None
    return None

admin = Blueprint('admin', __name__)

def generate_slug(name):
    """Generate a URL-safe slug from a name with a random suffix."""
    base_slug = name.lower().strip().replace(' ', '-')
    # Remove any non-alphanumeric characters except hyphens
    base_slug = ''.join(c for c in base_slug if c.isalnum() or c == '-')
    random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
    return f"{base_slug}-{random_suffix}"

@admin.before_request
def require_admin():
    """Protect all admin routes — must be logged in AND have admin role."""
    # Allow Flask-Login to handle the redirect for unauthenticated users
    if not current_user.is_authenticated:
        flash('Please log in to access the Inner Court.', 'error')
        return redirect(url_for('auth.login', next=request.url))
    if not current_user.is_admin():
        flash('You do not have permission to access the Inner Court.', 'error')
        return redirect(url_for('main.index'))

# ─────────────────────────────────────────────────────────────
# DASHBOARD
# ─────────────────────────────────────────────────────────────
@admin.route('/')
def dashboard():
    active_condition = ~Order.status.has(OrderStatus.name.in_(['Cancelled', 'Refunded']))
    total_orders = Order.query.filter(active_condition).count()
    total_revenue = db.session.query(db.func.sum(Order.total_amount)).filter(active_condition).scalar() or 0
    total_products = Product.query.count()
    low_stock_variants = ProductVariant.query.filter(ProductVariant.quantity <= 5).count()
    recent_orders = Order.query.order_by(Order.created_at.desc()).limit(10).all()
    return render_template('admin/dashboard.html',
                           total_orders=total_orders,
                           total_revenue=total_revenue,
                           total_products=total_products,
                           low_stock_variants=low_stock_variants,
                           recent_orders=recent_orders)

# ─────────────────────────────────────────────────────────────
# CATEGORIES
# ─────────────────────────────────────────────────────────────
@admin.route('/categories')
def manage_categories():
    categories = Category.query.all()
    return render_template('admin/categories.html', categories=categories)

@admin.route('/categories/add', methods=['GET', 'POST'])
def add_category():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        slug = request.form.get('slug', '').strip() or generate_slug(name)
        description = request.form.get('description', '').strip()
        parent_id = request.form.get('parent_id') or None

        if not name:
            flash('Category name is required.', 'error')
            return redirect(url_for('admin.add_category'))

        is_featured = 'is_featured' in request.form
        category = Category(name=name, slug=slug, description=description, parent_id=parent_id, is_featured=is_featured)
        db.session.add(category)
        db.session.commit()
        flash('Category created successfully.', 'success')
        return redirect(url_for('admin.manage_categories'))

    categories = Category.query.all()
    return render_template('admin/category_form.html', category=None, categories=categories)

@admin.route('/categories/<int:id>/edit', methods=['GET', 'POST'])
def edit_category(id):
    category = Category.query.get_or_404(id)
    if request.method == 'POST':
        category.name = request.form.get('name', '').strip()
        category.slug = request.form.get('slug', '').strip() or generate_slug(category.name)
        category.description = request.form.get('description', '').strip()
        parent_id = request.form.get('parent_id')
        category.parent_id = int(parent_id) if parent_id else None
        category.is_featured = 'is_featured' in request.form

        db.session.commit()
        flash('Category updated.', 'success')
        return redirect(url_for('admin.manage_categories'))

    categories = Category.query.all()
    return render_template('admin/category_form.html', category=category, categories=categories)

@admin.route('/categories/<int:id>/delete', methods=['POST'])
def delete_category(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    flash('Category deleted.', 'success')
    return redirect(url_for('admin.manage_categories'))

# ─────────────────────────────────────────────────────────────
# PRODUCTS
# ─────────────────────────────────────────────────────────────
@admin.route('/products')
def manage_products():
    products = Product.query.order_by(Product.created_at.desc()).all()
    return render_template('admin/products.html', products=products)

@admin.route('/products/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        price = request.form.get('price', '0')
        sku = request.form.get('sku', '').strip()
        short_desc = request.form.get('short_description', '').strip()
        description = request.form.get('description', '').strip()
        category_id = request.form.get('category_id') or None
        discount_price = request.form.get('discount_price', '').strip()
        stock_status = request.form.get('stock_status', 'in_stock')
        quantity = request.form.get('quantity', '0')
        is_featured = 'is_featured' in request.form

        if not name or not price or not sku:
            flash('Name, SKU and Price are required.', 'error')
            categories = Category.query.all()
            return render_template('admin/product_form.html', product=None, categories=categories)

        # Handle image upload
        image_url = None
        if 'main_image' in request.files:
            image_url = save_product_image(request.files['main_image'])

        product = Product(
            name=name,
            slug=generate_slug(name),
            price=float(price),
            sku=sku,
            short_description=short_desc,
            description=description,
            category_id=int(category_id) if category_id else None,
            discount_price=float(discount_price) if discount_price else None,
            stock_status=stock_status,
            quantity=int(quantity) if quantity else 0,
            is_featured=is_featured,
            main_image=image_url,
            status='active'
        )
        db.session.add(product)
        db.session.commit()
        flash('Timepiece forged successfully.', 'success')
        return redirect(url_for('admin.manage_products'))

    categories = Category.query.all()
    return render_template('admin/product_form.html', product=None, categories=categories)

@admin.route('/products/<int:id>/edit', methods=['GET', 'POST'])
def edit_product(id):
    product = Product.query.get_or_404(id)
    if request.method == 'POST':
        product.name = request.form.get('name', '').strip()
        product.price = float(request.form.get('price', '0'))
        product.sku = request.form.get('sku', '').strip()
        product.short_description = request.form.get('short_description', '').strip()
        product.description = request.form.get('description', '').strip()
        category_id = request.form.get('category_id')
        product.category_id = int(category_id) if category_id else None

        discount_price = request.form.get('discount_price', '').strip()
        product.discount_price = float(discount_price) if discount_price else None
        product.stock_status = request.form.get('stock_status', 'in_stock')
        quantity = request.form.get('quantity', '0')
        product.quantity = int(quantity) if quantity else 0
        product.is_featured = 'is_featured' in request.form

        # Handle image upload (only overwrite if new file provided)
        if 'main_image' in request.files and request.files['main_image'].filename:
            new_image = save_product_image(request.files['main_image'])
            if new_image:
                product.main_image = new_image

        db.session.commit()
        flash('Timepiece updated.', 'success')
        return redirect(url_for('admin.manage_products'))

    categories = Category.query.all()
    return render_template('admin/product_form.html', product=product, categories=categories)

@admin.route('/products/<int:id>/delete', methods=['POST'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    flash('Timepiece deleted.', 'success')
    return redirect(url_for('admin.manage_products'))

# ─────────────────────────────────────────────────────────────
# PRODUCT VARIANTS
# ─────────────────────────────────────────────────────────────
@admin.route('/products/<int:id>/variants')
def manage_product_variants(id):
    product = Product.query.get_or_404(id)
    return render_template('admin/product_manage.html', product=product)

@admin.route('/products/<int:id>/variants/add', methods=['GET', 'POST'])
def add_product_variant(id):
    product = Product.query.get_or_404(id)
    if request.method == 'POST':
        sku = request.form.get('sku', '').strip()
        color = request.form.get('color', '').strip()
        strap_type = request.form.get('strap_type', '').strip()
        size = request.form.get('size', '').strip()
        edition = request.form.get('edition', '').strip()
        price_override = request.form.get('price_override', '').strip()
        quantity = request.form.get('quantity', '0')

        if not sku:
            flash('Variant SKU is required.', 'error')
            return render_template('admin/variant_form.html', product=product, variant=None)

        # Handle image upload
        image_url = None
        if 'image' in request.files:
            image_url = save_product_image(request.files['image'])

        variant = ProductVariant(
            product_id=product.id,
            sku=sku,
            color=color or None,
            strap_type=strap_type or None,
            size=size or None,
            edition=edition or None,
            price_override=float(price_override) if price_override else None,
            quantity=int(quantity) if quantity else 0,
            image=image_url
        )
        db.session.add(variant)
        db.session.commit()
        flash('Variant forged successfully.', 'success')
        return redirect(url_for('admin.manage_product_variants', id=product.id))

    return render_template('admin/variant_form.html', product=product, variant=None)

@admin.route('/variants/<int:id>/edit', methods=['GET', 'POST'])
def edit_product_variant(id):
    variant = ProductVariant.query.get_or_404(id)
    product = variant.product
    
    if request.method == 'POST':
        variant.sku = request.form.get('sku', '').strip()
        variant.color = request.form.get('color', '').strip() or None
        variant.strap_type = request.form.get('strap_type', '').strip() or None
        variant.size = request.form.get('size', '').strip() or None
        variant.edition = request.form.get('edition', '').strip() or None
        
        price_override = request.form.get('price_override', '').strip()
        variant.price_override = float(price_override) if price_override else None
        
        quantity = request.form.get('quantity', '0')
        variant.quantity = int(quantity) if quantity else 0

        if 'image' in request.files and request.files['image'].filename:
            new_image = save_product_image(request.files['image'])
            if new_image:
                variant.image = new_image

        db.session.commit()
        flash('Variant updated.', 'success')
        return redirect(url_for('admin.manage_product_variants', id=product.id))

    return render_template('admin/variant_form.html', product=product, variant=variant)

@admin.route('/variants/<int:id>/delete', methods=['POST'])
def delete_product_variant(id):
    variant = ProductVariant.query.get_or_404(id)
    product_id = variant.product_id
    db.session.delete(variant)
    db.session.commit()
    flash('Variant deleted.', 'success')
    return redirect(url_for('admin.manage_product_variants', id=product_id))

# ─────────────────────────────────────────────────────────────
# COUPONS / DISCOUNTS
# ─────────────────────────────────────────────────────────────
@admin.route('/coupons')
def manage_coupons():
    coupons = Coupon.query.all()
    return render_template('admin/coupons.html', coupons=coupons)

@admin.route('/coupons/add', methods=['GET', 'POST'])
def add_coupon():
    if request.method == 'POST':
        code = request.form.get('code', '').strip().upper()
        discount_type = request.form.get('discount_type', 'percentage')
        discount_value = request.form.get('discount_value', '0')
        usage_limit = request.form.get('usage_limit', '').strip()

        if not code or not discount_value:
            flash('Code and discount value are required.', 'error')
            return render_template('admin/coupon_form.html', coupon=None)

        coupon = Coupon(
            code=code,
            discount_type=discount_type,
            discount_value=float(discount_value),
            usage_limit=int(usage_limit) if usage_limit else None
        )
        db.session.add(coupon)
        db.session.commit()
        flash('Coupon forged successfully.', 'success')
        return redirect(url_for('admin.manage_coupons'))
    return render_template('admin/coupon_form.html', coupon=None)

@admin.route('/coupons/<int:id>/edit', methods=['GET', 'POST'])
def edit_coupon(id):
    coupon = Coupon.query.get_or_404(id)
    if request.method == 'POST':
        coupon.code = request.form.get('code', '').strip().upper()
        coupon.discount_type = request.form.get('discount_type', 'percentage')
        coupon.discount_value = float(request.form.get('discount_value', '0'))
        usage_limit = request.form.get('usage_limit', '').strip()
        coupon.usage_limit = int(usage_limit) if usage_limit else None
        coupon.is_active = 'is_active' in request.form

        db.session.commit()
        flash('Coupon updated.', 'success')
        return redirect(url_for('admin.manage_coupons'))
    return render_template('admin/coupon_form.html', coupon=coupon)

@admin.route('/coupons/<int:id>/delete', methods=['POST'])
def delete_coupon(id):
    coupon = Coupon.query.get_or_404(id)
    db.session.delete(coupon)
    db.session.commit()
    flash('Coupon deleted.', 'success')
    return redirect(url_for('admin.manage_coupons'))

# ─────────────────────────────────────────────────────────────
# SHIPPING METHODS
# ─────────────────────────────────────────────────────────────
@admin.route('/shipping')
def manage_shipping():
    methods = ShippingMethod.query.all()
    return render_template('admin/shipping.html', methods=methods)

@admin.route('/shipping/add', methods=['GET', 'POST'])
def add_shipping():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        cost = request.form.get('cost', '0')
        delivery_estimate = request.form.get('delivery_estimate', '').strip()

        method = ShippingMethod(
            name=name,
            cost=float(cost),
            delivery_estimate=delivery_estimate or None
        )
        db.session.add(method)
        db.session.commit()
        flash('Shipping method added.', 'success')
        return redirect(url_for('admin.manage_shipping'))
    return render_template('admin/shipping_form.html', method=None)

@admin.route('/shipping/<int:id>/edit', methods=['GET', 'POST'])
def edit_shipping(id):
    method = ShippingMethod.query.get_or_404(id)
    if request.method == 'POST':
        method.name = request.form.get('name', '').strip()
        method.cost = float(request.form.get('cost', '0'))
        delivery_estimate = request.form.get('delivery_estimate', '').strip()
        method.delivery_estimate = delivery_estimate or None
        method.is_active = 'is_active' in request.form

        db.session.commit()
        flash('Shipping method updated.', 'success')
        return redirect(url_for('admin.manage_shipping'))
    return render_template('admin/shipping_form.html', method=method)

@admin.route('/shipping/<int:id>/delete', methods=['POST'])
def delete_shipping(id):
    method = ShippingMethod.query.get_or_404(id)
    db.session.delete(method)
    db.session.commit()
    flash('Shipping method deleted.', 'success')
    return redirect(url_for('admin.manage_shipping'))

# ─────────────────────────────────────────────────────────────
# PAYMENT METHODS
# ─────────────────────────────────────────────────────────────
@admin.route('/payment-methods')
def manage_payment_methods():
    methods = PaymentMethod.query.all()
    return render_template('admin/payment_methods.html', methods=methods)

@admin.route('/payment-methods/add', methods=['GET', 'POST'])
def add_payment_method():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        instructions = request.form.get('instructions', '').strip()

        method = PaymentMethod(name=name, instructions=instructions or None)
        db.session.add(method)
        db.session.commit()
        flash('Payment method added.', 'success')
        return redirect(url_for('admin.manage_payment_methods'))
    return render_template('admin/payment_form.html', method=None)

@admin.route('/payment-methods/<int:id>/edit', methods=['GET', 'POST'])
def edit_payment_method(id):
    method = PaymentMethod.query.get_or_404(id)
    if request.method == 'POST':
        method.name = request.form.get('name', '').strip()
        instructions = request.form.get('instructions', '').strip()
        method.instructions = instructions or None
        method.is_active = 'is_active' in request.form

        db.session.commit()
        flash('Payment method updated.', 'success')
        return redirect(url_for('admin.manage_payment_methods'))
    return render_template('admin/payment_form.html', method=method)

@admin.route('/payment-methods/<int:id>/delete', methods=['POST'])
def delete_payment_method(id):
    method = PaymentMethod.query.get_or_404(id)
    db.session.delete(method)
    db.session.commit()
    flash('Payment method deleted.', 'success')
    return redirect(url_for('admin.manage_payment_methods'))

# ─────────────────────────────────────────────────────────────
# ORDER STATUSES
# ─────────────────────────────────────────────────────────────
@admin.route('/order-statuses')
def manage_order_statuses():
    statuses = OrderStatus.query.all()
    return render_template('admin/order_statuses.html', statuses=statuses)

@admin.route('/order-statuses/add', methods=['GET', 'POST'])
def add_order_status():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        description = request.form.get('description', '').strip()

        status = OrderStatus(name=name, description=description or None)
        db.session.add(status)
        db.session.commit()
        flash('Order status added.', 'success')
        return redirect(url_for('admin.manage_order_statuses'))
    return render_template('admin/status_form.html', status=None)

@admin.route('/order-statuses/<int:id>/edit', methods=['GET', 'POST'])
def edit_order_status(id):
    status = OrderStatus.query.get_or_404(id)
    if request.method == 'POST':
        if not status.is_system:
            status.name = request.form.get('name', '').strip()
        description = request.form.get('description', '').strip()
        status.description = description or None

        db.session.commit()
        flash('Order status updated.', 'success')
        return redirect(url_for('admin.manage_order_statuses'))
    return render_template('admin/status_form.html', status=status)

@admin.route('/order-statuses/<int:id>/delete', methods=['POST'])
def delete_order_status(id):
    status = OrderStatus.query.get_or_404(id)
    if status.is_system:
        flash('System statuses cannot be deleted.', 'error')
        return redirect(url_for('admin.manage_order_statuses'))
    db.session.delete(status)
    db.session.commit()
    flash('Order status deleted.', 'success')
    return redirect(url_for('admin.manage_order_statuses'))

# ─────────────────────────────────────────────────────────────
# ORDERS
# ─────────────────────────────────────────────────────────────
@admin.route('/orders')
def manage_orders():
    orders = Order.query.order_by(Order.created_at.desc()).all()
    return render_template('admin/orders.html', orders=orders)

@admin.route('/orders/<int:id>')
def view_order(id):
    order = Order.query.get_or_404(id)
    statuses = OrderStatus.query.all()
    return render_template('admin/order_detail.html', order=order, statuses=statuses)

@admin.route('/orders/<int:id>/update-status', methods=['POST'])
def update_order_status(id):
    order = Order.query.get_or_404(id)
    status_id = request.form.get('order_status_id')
    
    if status_id:
        old_status = order.status
        new_status = OrderStatus.query.get(int(status_id))
        
        if old_status and new_status and old_status.id != new_status.id:
            cancelled_states = ['Cancelled', 'Refunded']
            was_cancelled = old_status.name in cancelled_states
            is_cancelled = new_status.name in cancelled_states
            
            # Transition: Active -> Cancelled (Restock items)
            if not was_cancelled and is_cancelled:
                for item in order.items:
                    if item.variant_id:
                        variant = ProductVariant.query.get(item.variant_id)
                        if variant:
                            variant.quantity += item.quantity
                    elif item.product_id:
                        product = Product.query.get(item.product_id)
                        if product:
                            product.quantity += item.quantity
            
            # Transition: Cancelled -> Active (Deduct items)
            elif was_cancelled and not is_cancelled:
                for item in order.items:
                    if item.variant_id:
                        variant = ProductVariant.query.get(item.variant_id)
                        if variant:
                            variant.quantity = max(0, variant.quantity - item.quantity)
                    elif item.product_id:
                        product = Product.query.get(item.product_id)
                        if product:
                            product.quantity = max(0, product.quantity - item.quantity)

        order.order_status_id = int(status_id)
        db.session.commit()
        flash('Order status updated.', 'success')
        
    return redirect(url_for('admin.view_order', id=id))
