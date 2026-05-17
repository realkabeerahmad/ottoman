from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'shop/checkout.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('base.html', 'shop/checkout.html')
    for name, parent_block in parent_template.blocks.items():
        context.blocks.setdefault(name, []).append(parent_block)
    yield from parent_template.root_render_func(context)

def block_content(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    _block_vars = {}
    l_0_url_for = resolve('url_for')
    l_0_current_user = resolve('current_user')
    l_0_shipping_methods = resolve('shipping_methods')
    l_0_payment_methods = resolve('payment_methods')
    l_0_cart_items = resolve('cart_items')
    l_0_config = resolve('config')
    l_0_subtotal = resolve('subtotal')
    try:
        t_1 = environment.filters['format']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'format' found.")
    pass
    yield '\n<section class="checkout-section" style="padding: 120px 4rem 8rem; max-width: 1200px; margin: 0 auto;">\n  <div class="section-header">\n    <span class="section-label">◆ Secure Acquisition ◆</span>\n    <h2 class="section-title">Finalize Order</h2>\n  </div>\n\n  <div class="checkout-grid">\n    <!-- Checkout Form -->\n    <div class="checkout-form-panel">\n      <h3 style="font-family: \'Cinzel\', serif; color: var(--gold); margin-bottom: 2rem;">Details of Recipient</h3>\n      \n      <form method="POST" action="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'shop.checkout', _block_vars=_block_vars))
    yield '" id="checkoutForm">\n        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-bottom: 2rem;">\n          <div>\n            <label style="display:block; font-family: \'Cinzel\', serif; font-size: 0.7rem; color: var(--text-muted); letter-spacing: 0.2em; text-transform: uppercase;">Full Name *</label>\n            <input type="text" name="name" required value="'
    if environment.getattr((undefined(name='current_user') if l_0_current_user is missing else l_0_current_user), 'is_authenticated'):
        pass
        yield escape(environment.getattr((undefined(name='current_user') if l_0_current_user is missing else l_0_current_user), 'full_name'))
    yield '" style="width: 100%; background: transparent; border: none; border-bottom: 1px solid var(--glass-border); color: var(--text-primary); padding: 0.5rem 0; font-family: \'Cormorant Garamond\', serif; font-size: 1.1rem; outline: none;">\n          </div>\n          <div>\n            <label style="display:block; font-family: \'Cinzel\', serif; font-size: 0.7rem; color: var(--text-muted); letter-spacing: 0.2em; text-transform: uppercase;">Email Address *</label>\n            <input type="email" name="email" required value="'
    if environment.getattr((undefined(name='current_user') if l_0_current_user is missing else l_0_current_user), 'is_authenticated'):
        pass
        yield escape(environment.getattr((undefined(name='current_user') if l_0_current_user is missing else l_0_current_user), 'email'))
    yield '" style="width: 100%; background: transparent; border: none; border-bottom: 1px solid var(--glass-border); color: var(--text-primary); padding: 0.5rem 0; font-family: \'Cormorant Garamond\', serif; font-size: 1.1rem; outline: none;">\n          </div>\n        </div>\n        \n        <div style="margin-bottom: 2rem;">\n          <label style="display:block; font-family: \'Cinzel\', serif; font-size: 0.7rem; color: var(--text-muted); letter-spacing: 0.2em; text-transform: uppercase;">Shipping Address *</label>\n          <input type="text" name="address" required style="width: 100%; background: transparent; border: none; border-bottom: 1px solid var(--glass-border); color: var(--text-primary); padding: 0.5rem 0; font-family: \'Cormorant Garamond\', serif; font-size: 1.1rem; outline: none;">\n        </div>\n        \n        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-bottom: 2rem;">\n          <div>\n            <label style="display:block; font-family: \'Cinzel\', serif; font-size: 0.7rem; color: var(--text-muted); letter-spacing: 0.2em; text-transform: uppercase;">City *</label>\n            <input type="text" name="city" required style="width: 100%; background: transparent; border: none; border-bottom: 1px solid var(--glass-border); color: var(--text-primary); padding: 0.5rem 0; font-family: \'Cormorant Garamond\', serif; font-size: 1.1rem; outline: none;">\n          </div>\n          <div>\n            <label style="display:block; font-family: \'Cinzel\', serif; font-size: 0.7rem; color: var(--text-muted); letter-spacing: 0.2em; text-transform: uppercase;">Phone Number</label>\n            <input type="text" name="phone" style="width: 100%; background: transparent; border: none; border-bottom: 1px solid var(--glass-border); color: var(--text-primary); padding: 0.5rem 0; font-family: \'Cormorant Garamond\', serif; font-size: 1.1rem; outline: none;">\n          </div>\n        </div>\n\n        '
    if (undefined(name='shipping_methods') if l_0_shipping_methods is missing else l_0_shipping_methods):
        pass
        yield '\n        <h3 style="font-family: \'Cinzel\', serif; color: var(--gold); margin-bottom: 1rem;">Shipping Method</h3>\n        <div style="margin-bottom: 2rem;">\n          '
        l_1_loop = missing
        for l_1_method, l_1_loop in LoopContext((undefined(name='shipping_methods') if l_0_shipping_methods is missing else l_0_shipping_methods), undefined):
            _loop_vars = {}
            pass
            yield '\n          <label style="display: flex; align-items: center; justify-content: space-between; gap: 1rem; color: var(--text-primary); font-family: \'Cinzel\', serif; font-size: 0.8rem; letter-spacing: 0.1em; padding: 0.8rem; border: 1px solid var(--glass-border); margin-bottom: 0.5rem; cursor: pointer;">\n            <div style="display: flex; align-items: center; gap: 0.8rem;">\n              <input type="radio" name="shipping_method_id" value="'
            yield escape(environment.getattr(l_1_method, 'id'))
            yield '" data-cost="'
            yield escape(environment.getattr(l_1_method, 'cost'))
            yield '" '
            if environment.getattr(l_1_loop, 'first'):
                pass
                yield 'checked'
            yield '>\n              '
            yield escape(environment.getattr(l_1_method, 'name'))
            yield '\n              '
            if environment.getattr(l_1_method, 'delivery_estimate'):
                pass
                yield '<small style="color: var(--text-dim);">('
                yield escape(environment.getattr(l_1_method, 'delivery_estimate'))
                yield ')</small>'
            yield '\n            </div>\n            <span class="shipping-cost-label" style="color: var(--gold);">'
            yield escape(environment.getattr((undefined(name='config') if l_0_config is missing else l_0_config), 'CURRENCY_SYMBOL'))
            yield escape(t_1('%.0f', environment.getattr(l_1_method, 'cost')))
            yield '</span>\n          </label>\n          '
        l_1_loop = l_1_method = missing
        yield '\n        </div>\n        '
    yield '\n\n        '
    if (undefined(name='payment_methods') if l_0_payment_methods is missing else l_0_payment_methods):
        pass
        yield '\n        <h3 style="font-family: \'Cinzel\', serif; color: var(--gold); margin-bottom: 1rem;">Payment Method</h3>\n        <div style="margin-bottom: 2rem;">\n          '
        l_1_loop = missing
        for l_1_method, l_1_loop in LoopContext((undefined(name='payment_methods') if l_0_payment_methods is missing else l_0_payment_methods), undefined):
            _loop_vars = {}
            pass
            yield '\n          <label style="display: flex; align-items: center; gap: 0.8rem; color: var(--text-primary); font-family: \'Cinzel\', serif; font-size: 0.8rem; letter-spacing: 0.1em; padding: 0.8rem; border: 1px solid var(--glass-border); margin-bottom: 0.5rem; cursor: pointer;">\n            <input type="radio" name="payment_method_id" value="'
            yield escape(environment.getattr(l_1_method, 'id'))
            yield '" '
            if environment.getattr(l_1_loop, 'first'):
                pass
                yield 'checked'
            yield '>\n            '
            yield escape(environment.getattr(l_1_method, 'name'))
            yield '\n            '
            if environment.getattr(l_1_method, 'instructions'):
                pass
                yield '<small style="color: var(--text-dim); margin-left: 0.5rem;">('
                yield escape(environment.getattr(l_1_method, 'instructions'))
                yield ')</small>'
            yield '\n          </label>\n          '
        l_1_loop = l_1_method = missing
        yield '\n        </div>\n        '
    else:
        pass
        yield '\n        <div style="margin-bottom: 2rem;">\n          <h3 style="font-family: \'Cinzel\', serif; color: var(--gold); margin-bottom: 1rem;">Payment Method</h3>\n          <label style="display: flex; align-items: center; gap: 1rem; color: var(--text-primary); font-family: \'Cinzel\', serif; font-size: 0.8rem; letter-spacing: 0.1em;">\n            <input type="radio" name="payment_method" value="cod" checked> Cash on Delivery\n          </label>\n        </div>\n        '
    yield '\n\n        <!-- Coupon Code (hidden field for actual coupon code, set by JS) -->\n        <input type="hidden" name="coupon_code" id="couponCodeHidden" value="">\n\n        <button type="submit" class="btn-primary" style="width: 100%;">Confirm Acquisition</button>\n      </form>\n    </div>\n\n    <!-- Order Summary -->\n    <div class="checkout-summary-panel">\n      <h3 style="font-family: \'Cinzel\', serif; color: var(--gold); margin-bottom: 2rem; border-bottom: 1px solid var(--glass-border); padding-bottom: 1rem;">Order Summary</h3>\n      \n      <div id="checkoutItems" style="margin-bottom: 2rem;">\n        '
    for l_1_item in (undefined(name='cart_items') if l_0_cart_items is missing else l_0_cart_items):
        _loop_vars = {}
        pass
        yield '\n        <div style="display: flex; justify-content: space-between; margin-bottom: 1rem; border-bottom: 1px solid var(--glass-border); padding-bottom: 1rem;">\n          <div>\n            <div style="font-family: \'Cinzel\', serif; font-size: 0.85rem; color: var(--text-primary);">'
        yield escape(environment.getattr(environment.getattr(l_1_item, 'product'), 'name'))
        yield '</div>\n            <div style="font-size: 0.8rem; color: var(--text-muted);">\n              Qty: '
        yield escape(environment.getattr(l_1_item, 'quantity'))
        yield '\n              '
        if (environment.getattr(environment.getattr(l_1_item, 'product'), 'discount_price') and (environment.getattr(environment.getattr(l_1_item, 'product'), 'discount_price') > 0)):
            pass
            yield '\n                · <span style="color: var(--gold);">'
            yield escape(environment.getattr((undefined(name='config') if l_0_config is missing else l_0_config), 'CURRENCY_SYMBOL'))
            yield escape(t_1('%.0f', environment.getattr(l_1_item, 'effective_price')))
            yield ' each</span>\n                <small style="text-decoration: line-through; color: var(--text-dim);">'
            yield escape(environment.getattr((undefined(name='config') if l_0_config is missing else l_0_config), 'CURRENCY_SYMBOL'))
            yield escape(t_1('%.0f', environment.getattr(environment.getattr(l_1_item, 'product'), 'price')))
            yield '</small>\n              '
        yield '\n            </div>\n          </div>\n          <div style="color: var(--gold); font-family: \'Cinzel\', serif;">'
        yield escape(environment.getattr((undefined(name='config') if l_0_config is missing else l_0_config), 'CURRENCY_SYMBOL'))
        yield escape(t_1('%.0f', environment.getattr(l_1_item, 'line_total')))
        yield '</div>\n        </div>\n        '
    l_1_item = missing
    yield '\n      </div>\n      \n      <div style="display: flex; justify-content: space-between; margin-bottom: 1rem; color: var(--text-muted);">\n        <span>Subtotal</span>\n        <span id="subtotalDisplay">'
    yield escape(environment.getattr((undefined(name='config') if l_0_config is missing else l_0_config), 'CURRENCY_SYMBOL'))
    yield escape(t_1('%.0f', (undefined(name='subtotal') if l_0_subtotal is missing else l_0_subtotal)))
    yield '</span>\n      </div>\n      <div style="display: flex; justify-content: space-between; margin-bottom: 1rem; color: var(--text-muted);">\n        <span>Shipping</span>\n        <span id="shippingCost">Select above</span>\n      </div>\n\n      <!-- Coupon discount row (hidden until applied) -->\n      <div id="discountRow" style="display: none; justify-content: space-between; margin-bottom: 1rem; color: var(--gold);">\n        <span>Discount <span id="discountLabel"></span></span>\n        <span id="discountAmount"></span>\n      </div>\n\n      <div style="border-top: 1px solid var(--glass-border); padding-top: 1rem; margin-bottom: 2rem;">\n        <div style="display: flex; justify-content: space-between; font-family: \'Cinzel\', serif; font-size: 1.2rem; color: var(--text-primary);">\n          <span>Total</span>\n          <span style="color: var(--gold);" id="orderTotal">'
    yield escape(environment.getattr((undefined(name='config') if l_0_config is missing else l_0_config), 'CURRENCY_SYMBOL'))
    yield escape(t_1('%.0f', (undefined(name='subtotal') if l_0_subtotal is missing else l_0_subtotal)))
    yield '</span>\n        </div>\n      </div>\n\n      <!-- Coupon Input -->\n      <div style="border-top: 1px solid var(--glass-border); padding-top: 1.5rem;">\n        <div style="font-family: \'Cinzel\', serif; font-size: 0.7rem; letter-spacing: 0.2em; text-transform: uppercase; color: var(--text-muted); margin-bottom: 0.8rem;">Have a Coupon?</div>\n        <div style="display: flex; gap: 0;">\n          <input type="text" id="couponInput" placeholder="Enter code..." style="flex: 1; background: transparent; border: 1px solid var(--glass-border); color: var(--text-primary); padding: 0.7rem 1rem; font-family: \'Cormorant Garamond\', serif; font-size: 1rem; outline: none; text-transform: uppercase;">\n          <button type="button" onclick="applyCoupon()" style="background: var(--gold); border: none; color: var(--obsidian); padding: 0.7rem 1.2rem; font-family: \'Cinzel\', serif; font-size: 0.65rem; letter-spacing: 0.15em; text-transform: uppercase; cursor: pointer; font-weight: 700;">Apply</button>\n        </div>\n        <div id="couponMsg" style="font-size: 0.85rem; margin-top: 0.5rem; font-style: italic;"></div>\n      </div>\n    </div>\n  </div>\n</section>\n'

def block_scripts(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    _block_vars = {}
    l_0_subtotal = resolve('subtotal')
    pass
    yield '\n<script>\nconst SUBTOTAL = '
    yield escape((undefined(name='subtotal') if l_0_subtotal is missing else l_0_subtotal))
    yield ';\nlet currentShipping = 0;\nlet currentDiscount = 0;\n\nfunction recalcTotal() {\n  const total = Math.max(SUBTOTAL + currentShipping - currentDiscount, 0);\n  document.getElementById(\'orderTotal\').textContent = CURRENCY + total.toFixed(0);\n}\n\n// Shipping selection\ndocument.querySelectorAll(\'input[name="shipping_method_id"]\').forEach(radio => {\n  radio.addEventListener(\'change\', function() {\n    currentShipping = parseFloat(this.dataset.cost) || 0;\n    document.getElementById(\'shippingCost\').textContent = CURRENCY + currentShipping.toFixed(0);\n    recalcTotal();\n  });\n  if (radio.checked) radio.dispatchEvent(new Event(\'change\'));\n});\n\n// Coupon\nfunction applyCoupon() {\n  const code = document.getElementById(\'couponInput\').value.trim();\n  const msg = document.getElementById(\'couponMsg\');\n  if (!code) { msg.textContent = \'Please enter a code.\'; msg.style.color = \'#c0392b\'; return; }\n\n  fetch(\'/shop/api/coupon/validate\', {\n    method: \'POST\',\n    headers: { \'Content-Type\': \'application/json\' },\n    body: JSON.stringify({ code: code, subtotal: SUBTOTAL })\n  })\n  .then(res => res.json())\n  .then(data => {\n    if (data.status === \'success\') {\n      currentDiscount = data.discount_amount;\n      document.getElementById(\'couponCodeHidden\').value = data.code;\n      document.getElementById(\'discountRow\').style.display = \'flex\';\n      document.getElementById(\'discountLabel\').textContent = \'(\' + data.code + \')\';\n      document.getElementById(\'discountAmount\').textContent = \'-\' + CURRENCY + currentDiscount.toFixed(0);\n      msg.textContent = data.message;\n      msg.style.color = \'var(--gold)\';\n      document.getElementById(\'couponInput\').disabled = true;\n      recalcTotal();\n    } else {\n      msg.textContent = data.message;\n      msg.style.color = \'#c0392b\';\n    }\n  })\n  .catch(() => {\n    msg.textContent = \'Failed to validate coupon.\';\n    msg.style.color = \'#c0392b\';\n  });\n}\n</script>\n'

blocks = {'content': block_content, 'scripts': block_scripts}
debug_info = '1=12&3=17&15=39&19=41&23=45&43=49&46=53&49=57&50=65&51=67&53=73&59=79&62=83&64=87&65=93&66=95&91=107&94=111&96=113&97=115&98=118&99=121&103=125&110=130&126=133&144=137&146=147'