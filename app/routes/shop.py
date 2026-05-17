from flask import Blueprint, render_template, jsonify, request, session, redirect, url_for, flash
from flask_login import current_user
from app import db
from app.models.product import Product, Category, ProductVariant
from app.models.cart import Cart, CartItem
from app.models.order import Order, OrderItem, ShippingMethod, PaymentMethod, Coupon
import uuid

shop = Blueprint('shop', __name__)

def get_or_create_cart():
    """Get the current user's cart, or create one. Supports both logged-in and guest users."""
    if current_user.is_authenticated:
        cart = Cart.query.filter_by(user_id=current_user.id).first()
        if not cart:
            cart = Cart(user_id=current_user.id)
            db.session.add(cart)
            db.session.commit()
        return cart
    else:
        if 'session_id' not in session:
            session['session_id'] = str(uuid.uuid4())
        cart = Cart.query.filter_by(session_id=session['session_id']).first()
        if not cart:
            cart = Cart(session_id=session['session_id'])
            db.session.add(cart)
            db.session.commit()
        return cart

# ─────────────────────────────────────────────────────────────
# COLLECTION & PRODUCT DETAIL
# ─────────────────────────────────────────────────────────────
@shop.route('/collection')
def collection():
    products = Product.query.filter_by(status='active').all()
    categories = Category.query.filter_by(status='active').all()
    featured_categories = Category.query.filter_by(is_featured=True, status='active').all()

    # Build parent->children slug map for hierarchical filtering
    # { "parent-slug": ["child1-slug", "child2-slug"], ... }
    category_tree = {}
    for cat in categories:
        if not cat.parent_id:
            child_slugs = [c.slug for c in cat.subcategories if c.status == 'active']
            category_tree[cat.slug] = child_slugs

    return render_template('shop/collection.html',
                           products=products,
                           categories=categories,
                           featured_categories=featured_categories,
                           category_tree=category_tree)

@shop.route('/product/<slug>')
def product_detail(slug):
    product = Product.query.filter_by(slug=slug, status='active').first_or_404()
    related = Product.query.filter(
        Product.category_id == product.category_id,
        Product.id != product.id,
        Product.status == 'active'
    ).limit(3).all() if product.category_id else []
    return render_template('shop/product_detail.html', product=product, related=related)

# ─────────────────────────────────────────────────────────────
# CART API
# ─────────────────────────────────────────────────────────────
@shop.route('/api/cart')
def get_cart():
    """Returns the current cart state as JSON."""
    cart = get_or_create_cart()
    items = []
    for item in cart.items:
        if item.product:
            image = item.product.main_image or ''
            name = item.product.name
            if item.variant:
                if item.variant.image:
                    image = item.variant.image
                variant_details = []
                if item.variant.color: variant_details.append(item.variant.color)
                if item.variant.strap_type: variant_details.append(item.variant.strap_type)
                if item.variant.size: variant_details.append(item.variant.size)
                if item.variant.edition: variant_details.append(item.variant.edition)
                if variant_details:
                    name += f" ({', '.join(variant_details)})"

            items.append({
                'id': item.id,
                'product_id': item.product_id,
                'variant_id': item.variant_id,
                'name': name,
                'slug': item.product.slug,
                'price': item.effective_price,
                'original_price': item.product.price,
                'has_discount': bool(item.product.discount_price and item.product.discount_price > 0),
                'quantity': item.quantity,
                'line_total': item.line_total,
                'image': image
            })
    return jsonify({
        'total_items': cart.total_items,
        'subtotal': cart.subtotal,
        'items': items
    })

@shop.route('/api/cart/add/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    cart = get_or_create_cart()
    product = Product.query.get_or_404(product_id)
    
    data = request.get_json(silent=True) or {}
    variant_id = data.get('variant_id')
    
    variant = None
    if variant_id:
        variant = ProductVariant.query.get(variant_id)

    # Stock check
    stock_qty = variant.quantity if variant else product.quantity
    if stock_qty <= 0:
        return jsonify({'status': 'error', 'message': 'This item is out of stock.'}), 400

    cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product.id, variant_id=variant_id).first()
    if cart_item:
        if cart_item.quantity + 1 > stock_qty:
            return jsonify({'status': 'error', 'message': f'Only {stock_qty} units available.'}), 400
        cart_item.quantity += 1
    else:
        cart_item = CartItem(cart_id=cart.id, product_id=product.id, variant_id=variant_id, quantity=1)
        db.session.add(cart_item)

    db.session.commit()

    display_name = variant.sku if variant else product.name
    return jsonify({
        'status': 'success',
        'message': f'✦ {display_name} added to collection',
        'cart_count': cart.total_items
    })

@shop.route('/api/cart/update/<int:item_id>', methods=['POST'])
def update_cart_item(item_id):
    """Update quantity of a cart item. Send JSON { "quantity": N }"""
    cart = get_or_create_cart()
    cart_item = CartItem.query.filter_by(id=item_id, cart_id=cart.id).first_or_404()

    data = request.get_json(silent=True) or {}
    new_qty = data.get('quantity', 1)

    if isinstance(new_qty, str):
        new_qty = int(new_qty) if new_qty.isdigit() else 1

    if new_qty <= 0:
        db.session.delete(cart_item)
        db.session.commit()
        return jsonify({
            'status': 'success',
            'message': '✦ Item removed',
            'cart_count': cart.total_items,
            'subtotal': cart.subtotal
        })

    if cart_item.variant:
        max_qty = cart_item.variant.quantity
    elif cart_item.product:
        max_qty = cart_item.product.quantity
    else:
        max_qty = 0

    if new_qty > max_qty:
        return jsonify({'status': 'error', 'message': f'Only {max_qty} units available.'}), 400

    cart_item.quantity = new_qty
    db.session.commit()

    return jsonify({
        'status': 'success',
        'message': f'✦ Quantity updated to {new_qty}',
        'cart_count': cart.total_items,
        'subtotal': cart.subtotal
    })

@shop.route('/api/cart/remove/<int:item_id>', methods=['POST'])
def remove_from_cart(item_id):
    cart = get_or_create_cart()
    cart_item = CartItem.query.filter_by(id=item_id, cart_id=cart.id).first_or_404()
    name = cart_item.product.name if cart_item.product else 'Item'
    db.session.delete(cart_item)
    db.session.commit()
    return jsonify({
        'status': 'success',
        'message': f'✦ {name} removed',
        'cart_count': cart.total_items,
        'subtotal': cart.subtotal
    })

# ─────────────────────────────────────────────────────────────
# COUPON VALIDATION API
# ─────────────────────────────────────────────────────────────
@shop.route('/api/coupon/validate', methods=['POST'])
def validate_coupon():
    """Validate a coupon code and return its discount info."""
    data = request.get_json(silent=True) or {}
    code = data.get('code', '').strip().upper()
    subtotal = float(data.get('subtotal', 0))

    if not code:
        return jsonify({'status': 'error', 'message': 'Please enter a coupon code.'}), 400

    coupon = Coupon.query.filter_by(code=code, is_active=True).first()
    if not coupon:
        return jsonify({'status': 'error', 'message': 'Invalid coupon code.'}), 400

    if coupon.usage_limit and coupon.times_used >= coupon.usage_limit:
        return jsonify({'status': 'error', 'message': 'This coupon has been fully redeemed.'}), 400

    # Calculate discount
    if coupon.discount_type == 'percentage':
        discount = round(subtotal * (coupon.discount_value / 100), 2)
        desc = f'{coupon.discount_value}% off'
    else:
        discount = min(coupon.discount_value, subtotal)
        desc = f'${coupon.discount_value} off'

    return jsonify({
        'status': 'success',
        'message': f'✦ Coupon applied: {desc}',
        'coupon_id': coupon.id,
        'code': coupon.code,
        'discount_type': coupon.discount_type,
        'discount_value': coupon.discount_value,
        'discount_amount': discount
    })

# ─────────────────────────────────────────────────────────────
# CHECKOUT
# ─────────────────────────────────────────────────────────────
@shop.route('/checkout', methods=['GET', 'POST'])
def checkout():
    cart = get_or_create_cart()

    if cart.total_items == 0:
        flash('Your collection is empty.', 'info')
        return redirect(url_for('shop.collection'))

    shipping_methods = ShippingMethod.query.filter_by(is_active=True).all()
    payment_methods = PaymentMethod.query.filter_by(is_active=True).all()

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        phone = request.form.get('phone', '').strip()
        address = request.form.get('address', '').strip()
        city = request.form.get('city', '').strip()

        if not all([name, email, address, city]):
            flash('Please fill in all required fields.', 'error')
            return render_template('shop/checkout.html',
                                   cart_items=cart.items,
                                   subtotal=cart.subtotal,
                                   shipping_methods=shipping_methods,
                                   payment_methods=payment_methods)

        # ── Subtotal (already uses effective_price via cart model)
        subtotal = cart.subtotal

        # ── Shipping
        shipping_cost = 0.0
        shipping_method_id = request.form.get('shipping_method_id')
        if shipping_method_id:
            sm = ShippingMethod.query.get(int(shipping_method_id))
            if sm:
                shipping_cost = sm.cost

        # ── Coupon
        discount_amount = 0.0
        coupon_id = None
        coupon_code = request.form.get('coupon_code', '').strip().upper()
        if coupon_code:
            coupon = Coupon.query.filter_by(code=coupon_code, is_active=True).first()
            if coupon and (not coupon.usage_limit or coupon.times_used < coupon.usage_limit):
                if coupon.discount_type == 'percentage':
                    discount_amount = round(subtotal * (coupon.discount_value / 100), 2)
                else:
                    discount_amount = min(coupon.discount_value, subtotal)
                coupon_id = coupon.id
                coupon.times_used += 1

        # ── Payment
        payment_method_id = request.form.get('payment_method_id')

        # ── Total
        total = max(subtotal + shipping_cost - discount_amount, 0)

        # ── Create Order
        order = Order(
            user_id=current_user.id if current_user.is_authenticated else None,
            customer_name=name,
            customer_email=email,
            customer_phone=phone,
            shipping_address=address,
            shipping_city=city,
            subtotal=subtotal,
            shipping_cost=shipping_cost,
            discount_amount=discount_amount,
            total_amount=total,
            shipping_method_id=int(shipping_method_id) if shipping_method_id else None,
            payment_method_id=int(payment_method_id) if payment_method_id else None,
            coupon_id=coupon_id
        )
        db.session.add(order)
        db.session.flush()

        for item in cart.items:
            order_item = OrderItem(
                order_id=order.id,
                product_id=item.product_id,
                variant_id=item.variant_id,
                product_name=item.product.name,
                sku=item.variant.sku if item.variant else item.product.sku,
                price=item.effective_price,
                quantity=item.quantity
            )
            db.session.add(order_item)
            
            # Decrease stock
            if item.variant:
                if item.variant.quantity >= item.quantity:
                    item.variant.quantity -= item.quantity
                else:
                    item.variant.quantity = 0
            elif item.product:
                if item.product.quantity >= item.quantity:
                    item.product.quantity -= item.quantity
                else:
                    item.product.quantity = 0

        # Clear Cart
        for item in cart.items:
            db.session.delete(item)

        db.session.commit()

        flash(f'Order #{order.order_number} confirmed. Thank you for your acquisition.', 'success')
        return redirect(url_for('main.index'))

    return render_template('shop/checkout.html',
                           cart_items=cart.items,
                           subtotal=cart.subtotal,
                           shipping_methods=shipping_methods,
                           payment_methods=payment_methods)
