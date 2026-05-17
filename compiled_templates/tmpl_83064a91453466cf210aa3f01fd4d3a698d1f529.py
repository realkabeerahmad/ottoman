from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'admin/order_detail.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('admin/admin_base.html', 'admin/order_detail.html')
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
    l_0_order = resolve('order')
    l_0_url_for = resolve('url_for')
    l_0_statuses = resolve('statuses')
    l_0_config = resolve('config')
    try:
        t_1 = environment.filters['format']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'format' found.")
    pass
    yield '\n<div class="page-header">\n  <div>\n    <h1 class="page-title">Order #'
    yield escape(environment.getattr((undefined(name='order') if l_0_order is missing else l_0_order), 'order_number'))
    yield '</h1>\n    <div class="page-subtitle">Placed '
    yield escape(context.call(environment.getattr(environment.getattr((undefined(name='order') if l_0_order is missing else l_0_order), 'created_at'), 'strftime'), '%d %b %Y at %H:%M', _block_vars=_block_vars))
    yield '</div>\n  </div>\n  <div>\n    <form method="POST" action="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.update_order_status', id=environment.getattr((undefined(name='order') if l_0_order is missing else l_0_order), 'id'), _block_vars=_block_vars))
    yield '" style="display: flex; gap: 0.8rem; align-items: center;">\n      <select name="order_status_id" class="form-select" style="width: auto; min-width: 160px;">\n        <option value="">— Select Status —</option>\n        '
    for l_1_s in (undefined(name='statuses') if l_0_statuses is missing else l_0_statuses):
        _loop_vars = {}
        pass
        yield '\n        <option value="'
        yield escape(environment.getattr(l_1_s, 'id'))
        yield '" '
        if (environment.getattr((undefined(name='order') if l_0_order is missing else l_0_order), 'order_status_id') == environment.getattr(l_1_s, 'id')):
            pass
            yield 'selected'
        yield '>'
        yield escape(environment.getattr(l_1_s, 'name'))
        yield '</option>\n        '
    l_1_s = missing
    yield '\n      </select>\n      <button type="submit" class="btn-admin-primary" style="padding: 0.6rem 1.2rem;">Update</button>\n    </form>\n  </div>\n</div>\n\n<div style="display: grid; grid-template-columns: 2fr 1fr; gap: 2rem;">\n  <!-- Items Table -->\n  <div>\n    <h3 style="font-family: \'Cinzel\', serif; color: var(--gold); margin-bottom: 1rem; font-size: 1rem;">Order Items</h3>\n    <table class="data-table">\n      <thead>\n        <tr>\n          <th>Product</th>\n          <th>SKU</th>\n          <th>Price</th>\n          <th>Qty</th>\n          <th>Line Total</th>\n        </tr>\n      </thead>\n      <tbody>\n        '
    for l_1_item in environment.getattr((undefined(name='order') if l_0_order is missing else l_0_order), 'items'):
        _loop_vars = {}
        pass
        yield '\n        <tr>\n          <td>'
        yield escape(environment.getattr(l_1_item, 'product_name'))
        yield '</td>\n          <td class="mono muted">'
        yield escape((environment.getattr(l_1_item, 'sku') or '—'))
        yield '</td>\n          <td class="gold">'
        yield escape(environment.getattr((undefined(name='config') if l_0_config is missing else l_0_config), 'CURRENCY_SYMBOL'))
        yield escape(t_1('%.2f', environment.getattr(l_1_item, 'price')))
        yield '</td>\n          <td>'
        yield escape(environment.getattr(l_1_item, 'quantity'))
        yield '</td>\n          <td class="gold">'
        yield escape(environment.getattr((undefined(name='config') if l_0_config is missing else l_0_config), 'CURRENCY_SYMBOL'))
        yield escape(t_1('%.2f', (environment.getattr(l_1_item, 'price') * environment.getattr(l_1_item, 'quantity'))))
        yield '</td>\n        </tr>\n        '
    l_1_item = missing
    yield '\n      </tbody>\n    </table>\n  </div>\n\n  <!-- Sidebar Details -->\n  <div style="display: flex; flex-direction: column; gap: 1.5rem;">\n    <!-- Customer -->\n    <div class="stat-card">\n      <div class="stat-label">Customer</div>\n      <div style="color: rgba(255,255,255,0.85); font-family: \'Cormorant Garamond\', serif; font-size: 1.1rem; margin-bottom: 0.5rem;">'
    yield escape(environment.getattr((undefined(name='order') if l_0_order is missing else l_0_order), 'customer_name'))
    yield '</div>\n      <div class="muted" style="font-size: 0.9rem;">'
    yield escape(environment.getattr((undefined(name='order') if l_0_order is missing else l_0_order), 'customer_email'))
    yield '</div>\n      '
    if environment.getattr((undefined(name='order') if l_0_order is missing else l_0_order), 'customer_phone'):
        pass
        yield '\n      <div class="muted" style="font-size: 0.9rem;">'
        yield escape(environment.getattr((undefined(name='order') if l_0_order is missing else l_0_order), 'customer_phone'))
        yield '</div>\n      '
    yield '\n    </div>\n\n    <!-- Shipping -->\n    <div class="stat-card">\n      <div class="stat-label">Shipping Address</div>\n      <div style="color: rgba(255,255,255,0.7); font-family: \'Cormorant Garamond\', serif; font-size: 1rem; line-height: 1.6;">\n        '
    yield escape(environment.getattr((undefined(name='order') if l_0_order is missing else l_0_order), 'shipping_address'))
    yield '<br>\n        '
    yield escape(environment.getattr((undefined(name='order') if l_0_order is missing else l_0_order), 'shipping_city'))
    yield '\n        '
    if environment.getattr((undefined(name='order') if l_0_order is missing else l_0_order), 'shipping_postal_code'):
        pass
        yield ', '
        yield escape(environment.getattr((undefined(name='order') if l_0_order is missing else l_0_order), 'shipping_postal_code'))
    yield '<br>\n        '
    yield escape(environment.getattr((undefined(name='order') if l_0_order is missing else l_0_order), 'shipping_country'))
    yield '\n      </div>\n      '
    if environment.getattr((undefined(name='order') if l_0_order is missing else l_0_order), 'shipping_method'):
        pass
        yield '\n      <div style="margin-top: 0.8rem; font-family: \'Cinzel\', serif; font-size: 0.7rem; color: var(--gold); text-transform: uppercase; letter-spacing: 0.1em;">\n        Via: '
        yield escape(environment.getattr(environment.getattr((undefined(name='order') if l_0_order is missing else l_0_order), 'shipping_method'), 'name'))
        yield '\n      </div>\n      '
    yield '\n    </div>\n\n    <!-- Financials -->\n    <div class="stat-card">\n      <div class="stat-label">Financials</div>\n      <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">\n        <span class="muted">Subtotal</span>\n        <span style="color: rgba(255,255,255,0.7);">'
    yield escape(environment.getattr((undefined(name='config') if l_0_config is missing else l_0_config), 'CURRENCY_SYMBOL'))
    yield escape(t_1('%.2f', environment.getattr((undefined(name='order') if l_0_order is missing else l_0_order), 'subtotal')))
    yield '</span>\n      </div>\n      <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">\n        <span class="muted">Shipping</span>\n        <span style="color: rgba(255,255,255,0.7);">'
    yield escape(environment.getattr((undefined(name='config') if l_0_config is missing else l_0_config), 'CURRENCY_SYMBOL'))
    yield escape(t_1('%.2f', environment.getattr((undefined(name='order') if l_0_order is missing else l_0_order), 'shipping_cost')))
    yield '</span>\n      </div>\n      '
    if (environment.getattr((undefined(name='order') if l_0_order is missing else l_0_order), 'discount_amount') > 0):
        pass
        yield '\n      <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">\n        <span style="color: var(--gold);">Discount'
        if environment.getattr((undefined(name='order') if l_0_order is missing else l_0_order), 'coupon'):
            pass
            yield ' ('
            yield escape(environment.getattr(environment.getattr((undefined(name='order') if l_0_order is missing else l_0_order), 'coupon'), 'code'))
            yield ')'
        yield '</span>\n        <span style="color: var(--gold);">-'
        yield escape(environment.getattr((undefined(name='config') if l_0_config is missing else l_0_config), 'CURRENCY_SYMBOL'))
        yield escape(t_1('%.2f', environment.getattr((undefined(name='order') if l_0_order is missing else l_0_order), 'discount_amount')))
        yield '</span>\n      </div>\n      '
    yield '\n      <hr style="border: none; border-top: 1px solid rgba(201,168,76,0.1); margin: 0.8rem 0;">\n      <div style="display: flex; justify-content: space-between; align-items: center;">\n        <span style="font-family: \'Cinzel\', serif; font-weight: bold; color: rgba(255,255,255,0.85);">Total</span>\n        <span style="color: var(--gold); font-size: 1.4rem; font-family: \'Cinzel Decorative\', serif;">'
    yield escape(environment.getattr((undefined(name='config') if l_0_config is missing else l_0_config), 'CURRENCY_SYMBOL'))
    yield escape(t_1('%.2f', environment.getattr((undefined(name='order') if l_0_order is missing else l_0_order), 'total_amount')))
    yield '</span>\n      </div>\n    </div>\n  </div>\n</div>\n'

blocks = {'content': block_content}
debug_info = '1=12&3=17&6=36&7=38&10=40&13=42&14=46&37=56&39=60&40=62&41=64&42=67&43=69&55=74&56=76&57=78&58=81&66=84&67=86&68=88&69=93&71=95&73=98&83=101&87=104&89=107&91=110&92=116&98=120'