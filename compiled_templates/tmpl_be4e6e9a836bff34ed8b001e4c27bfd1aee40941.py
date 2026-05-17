from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'admin/coupons.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('admin/admin_base.html', 'admin/coupons.html')
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
    l_0_coupons = resolve('coupons')
    try:
        t_1 = environment.filters['format']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'format' found.")
    pass
    yield '\n<div class="page-header">\n  <div>\n    <h1 class="page-title">Discounts & Coupons</h1>\n    <div class="page-subtitle">Manage promotional codes</div>\n  </div>\n  <a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.add_coupon', _block_vars=_block_vars))
    yield '" class="btn-admin-primary">+ Add Coupon</a>\n</div>\n\n<table class="data-table">\n  <thead>\n    <tr>\n      <th>Code</th>\n      <th>Type</th>\n      <th>Value</th>\n      <th>Usage</th>\n      <th>Active</th>\n      <th>Actions</th>\n    </tr>\n  </thead>\n  <tbody>\n    '
    t_2 = 1
    for l_1_coupon in (undefined(name='coupons') if l_0_coupons is missing else l_0_coupons):
        l_1_config = resolve('config')
        _loop_vars = {}
        pass
        yield '\n    <tr>\n      <td style="font-weight: bold; letter-spacing: 0.1em;">'
        yield escape(environment.getattr(l_1_coupon, 'code'))
        yield '</td>\n      <td class="muted" style="text-transform: uppercase; font-size: 0.85rem;">'
        yield escape(environment.getattr(l_1_coupon, 'discount_type'))
        yield '</td>\n      <td class="gold">\n        '
        if (environment.getattr(l_1_coupon, 'discount_type') == 'percentage'):
            pass
            yield escape(environment.getattr(l_1_coupon, 'discount_value'))
            yield '%'
        else:
            pass
            yield escape(environment.getattr((undefined(name='config') if l_1_config is missing else l_1_config), 'CURRENCY_SYMBOL'))
            yield escape(t_1('%.2f', environment.getattr(l_1_coupon, 'discount_value')))
        yield '\n      </td>\n      <td class="muted">'
        yield escape(environment.getattr(l_1_coupon, 'times_used'))
        yield ' / '
        yield escape((environment.getattr(l_1_coupon, 'usage_limit') if environment.getattr(l_1_coupon, 'usage_limit') else '∞'))
        yield '</td>\n      <td><span class="badge '
        if environment.getattr(l_1_coupon, 'is_active'):
            pass
            yield 'badge-active'
        else:
            pass
            yield 'badge-inactive'
        yield '">'
        yield escape(('Yes' if environment.getattr(l_1_coupon, 'is_active') else 'No'))
        yield '</span></td>\n      <td>\n        <form class="delete-form" method="POST" action="'
        yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.delete_coupon', id=environment.getattr(l_1_coupon, 'id'), _loop_vars=_loop_vars))
        yield '" onsubmit="return confirm(\'Delete this coupon?\');">\n          <button type="submit">Delete</button>\n        </form>\n      </td>\n    </tr>\n    '
        t_2 = 0
    l_1_coupon = l_1_config = missing
    if t_2:
        pass
        yield '\n    <tr class="empty-row"><td colspan="6">No coupons configured.</td></tr>\n    '
    yield '\n  </tbody>\n</table>\n'

blocks = {'content': block_content}
debug_info = '1=12&3=17&9=34&24=37&26=42&27=44&29=46&31=55&32=59&34=68'