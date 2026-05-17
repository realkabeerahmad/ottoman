from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'admin/orders.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('admin/admin_base.html', 'admin/orders.html')
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
    l_0_orders = resolve('orders')
    try:
        t_1 = environment.filters['format']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'format' found.")
    pass
    yield '\n<div class="page-header">\n  <div>\n    <h1 class="page-title">Orders</h1>\n    <div class="page-subtitle">Manage customer acquisitions</div>\n  </div>\n</div>\n\n<table class="data-table">\n  <thead>\n    <tr>\n      <th>Order #</th>\n      <th>Date</th>\n      <th>Customer</th>\n      <th>Items</th>\n      <th>Total</th>\n      <th>Status</th>\n      <th>Actions</th>\n    </tr>\n  </thead>\n  <tbody>\n    '
    t_2 = 1
    for l_1_order in (undefined(name='orders') if l_0_orders is missing else l_0_orders):
        l_1_config = resolve('config')
        l_1_url_for = resolve('url_for')
        _loop_vars = {}
        pass
        yield '\n    <tr>\n      <td class="mono">'
        yield escape(environment.getattr(l_1_order, 'order_number'))
        yield '</td>\n      <td class="muted">'
        yield escape(context.call(environment.getattr(environment.getattr(l_1_order, 'created_at'), 'strftime'), '%d %b %Y, %H:%M', _loop_vars=_loop_vars))
        yield '</td>\n      <td>'
        yield escape(environment.getattr(l_1_order, 'customer_name'))
        yield '<br><small class="muted">'
        yield escape(environment.getattr(l_1_order, 'customer_email'))
        yield '</small></td>\n      <td class="muted">'
        yield escape(context.call(environment.getattr(environment.getattr(l_1_order, 'items'), 'count'), _loop_vars=_loop_vars))
        yield ' items</td>\n      <td class="gold">'
        yield escape(environment.getattr((undefined(name='config') if l_1_config is missing else l_1_config), 'CURRENCY_SYMBOL'))
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
        yield escape(context.call((undefined(name='url_for') if l_1_url_for is missing else l_1_url_for), 'admin.view_order', id=environment.getattr(l_1_order, 'id'), _loop_vars=_loop_vars))
        yield '" class="action-link view">View Details</a></td>\n    </tr>\n    '
        t_2 = 0
    l_1_order = l_1_config = l_1_url_for = missing
    if t_2:
        pass
        yield '\n    <tr class="empty-row"><td colspan="7">No orders found.</td></tr>\n    '
    yield '\n  </tbody>\n</table>\n'

blocks = {'content': block_content}
debug_info = '1=12&3=17&24=34&26=40&27=42&28=44&29=48&30=50&32=53&33=56&35=61&38=64'