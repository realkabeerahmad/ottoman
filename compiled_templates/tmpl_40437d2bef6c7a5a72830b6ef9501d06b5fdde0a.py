from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'admin/dashboard.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('admin/admin_base.html', 'admin/dashboard.html')
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
    l_0_total_orders = resolve('total_orders')
    l_0_config = resolve('config')
    l_0_total_revenue = resolve('total_revenue')
    l_0_total_products = resolve('total_products')
    l_0_low_stock_variants = resolve('low_stock_variants')
    l_0_url_for = resolve('url_for')
    l_0_recent_orders = resolve('recent_orders')
    try:
        t_1 = environment.filters['format']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'format' found.")
    pass
    yield '\n<div class="page-header">\n  <div>\n    <h1 class="page-title">Dashboard</h1>\n    <div class="page-subtitle">Overview of your empire</div>\n  </div>\n</div>\n\n<div class="stats-grid">\n  <div class="stat-card">\n    <div class="stat-label">Total Acquisitions</div>\n    <div class="stat-value">'
    yield escape((undefined(name='total_orders') if l_0_total_orders is missing else l_0_total_orders))
    yield '</div>\n  </div>\n  <div class="stat-card">\n    <div class="stat-label">Imperial Treasury</div>\n    <div class="stat-value">'
    yield escape(environment.getattr((undefined(name='config') if l_0_config is missing else l_0_config), 'CURRENCY_SYMBOL'))
    yield escape(t_1('%.2f', (undefined(name='total_revenue') if l_0_total_revenue is missing else l_0_total_revenue)))
    yield '</div>\n  </div>\n  <div class="stat-card">\n    <div class="stat-label">Timepieces in Catalog</div>\n    <div class="stat-value">'
    yield escape((undefined(name='total_products') if l_0_total_products is missing else l_0_total_products))
    yield '</div>\n  </div>\n  <div class="stat-card">\n    <div class="stat-label">Low Stock Variants</div>\n    <div class="stat-value" style="color: '
    if ((undefined(name='low_stock_variants') if l_0_low_stock_variants is missing else l_0_low_stock_variants) > 0):
        pass
        yield '#e74c3c'
    else:
        pass
        yield 'var(--gold)'
    yield ';">'
    yield escape((undefined(name='low_stock_variants') if l_0_low_stock_variants is missing else l_0_low_stock_variants))
    yield '</div>\n  </div>\n</div>\n\n<div class="page-header" style="border-bottom: none; padding-bottom: 0;">\n  <h2 style="font-family: \'Cinzel\', serif; color: var(--gold); font-size: 1.1rem;">Recent Orders</h2>\n  <a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.manage_orders', _block_vars=_block_vars))
    yield '" class="action-link view">View All →</a>\n</div>\n\n<table class="data-table">\n  <thead>\n    <tr>\n      <th>Order #</th>\n      <th>Date</th>\n      <th>Customer</th>\n      <th>Total</th>\n      <th>Status</th>\n      <th>Actions</th>\n    </tr>\n  </thead>\n  <tbody>\n    '
    t_2 = 1
    for l_1_order in (undefined(name='recent_orders') if l_0_recent_orders is missing else l_0_recent_orders):
        _loop_vars = {}
        pass
        yield '\n    <tr>\n      <td class="mono">'
        yield escape(environment.getattr(l_1_order, 'order_number'))
        yield '</td>\n      <td class="muted">'
        yield escape(context.call(environment.getattr(environment.getattr(l_1_order, 'created_at'), 'strftime'), '%d %b %Y', _loop_vars=_loop_vars))
        yield '</td>\n      <td>'
        yield escape(environment.getattr(l_1_order, 'customer_name'))
        yield '</td>\n      <td class="gold">'
        yield escape(environment.getattr((undefined(name='config') if l_0_config is missing else l_0_config), 'CURRENCY_SYMBOL'))
        yield escape(t_1('%.2f', environment.getattr(l_1_order, 'total_amount')))
        yield '</td>\n      <td>\n        '
        if environment.getattr(l_1_order, 'status'):
            pass
            yield '\n          <span class="badge badge-active">'
            yield escape(environment.getattr(environment.getattr(l_1_order, 'status'), 'name'))
            yield '</span>\n        '
        else:
            pass
            yield '\n          <span class="badge badge-warning">'
            yield escape(environment.getattr(l_1_order, 'status_string'))
            yield '</span>\n        '
        yield '\n      </td>\n      <td><a href="'
        yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.view_order', id=environment.getattr(l_1_order, 'id'), _loop_vars=_loop_vars))
        yield '" class="action-link view">View</a></td>\n    </tr>\n    '
        t_2 = 0
    l_1_order = missing
    if t_2:
        pass
        yield '\n    <tr class="empty-row"><td colspan="6">No orders yet. Your empire awaits its first conquest.</td></tr>\n    '
    yield '\n  </tbody>\n</table>\n'

blocks = {'content': block_content}
debug_info = '1=12&3=17&14=39&18=41&22=44&26=46&32=55&47=58&49=62&50=64&51=66&52=68&54=71&55=74&57=79&60=82'