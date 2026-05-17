from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'admin/shipping.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('admin/admin_base.html', 'admin/shipping.html')
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
    l_0_methods = resolve('methods')
    try:
        t_1 = environment.filters['format']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'format' found.")
    pass
    yield '\n<div class="page-header">\n  <div>\n    <h1 class="page-title">Shipping Methods</h1>\n    <div class="page-subtitle">Configure delivery options</div>\n  </div>\n  <a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.add_shipping', _block_vars=_block_vars))
    yield '" class="btn-admin-primary">+ Add Method</a>\n</div>\n\n<table class="data-table">\n  <thead>\n    <tr>\n      <th>Name</th>\n      <th>Cost</th>\n      <th>Delivery Estimate</th>\n      <th>Active</th>\n      <th>Actions</th>\n    </tr>\n  </thead>\n  <tbody>\n    '
    t_2 = 1
    for l_1_method in (undefined(name='methods') if l_0_methods is missing else l_0_methods):
        l_1_config = resolve('config')
        _loop_vars = {}
        pass
        yield '\n    <tr>\n      <td>'
        yield escape(environment.getattr(l_1_method, 'name'))
        yield '</td>\n      <td class="gold">'
        yield escape(environment.getattr((undefined(name='config') if l_1_config is missing else l_1_config), 'CURRENCY_SYMBOL'))
        yield escape(t_1('%.2f', environment.getattr(l_1_method, 'cost')))
        yield '</td>\n      <td class="muted">'
        yield escape((environment.getattr(l_1_method, 'delivery_estimate') or '—'))
        yield '</td>\n      <td><span class="badge '
        if environment.getattr(l_1_method, 'is_active'):
            pass
            yield 'badge-active'
        else:
            pass
            yield 'badge-inactive'
        yield '">'
        yield escape(('Yes' if environment.getattr(l_1_method, 'is_active') else 'No'))
        yield '</span></td>\n      <td>\n        <form class="delete-form" method="POST" action="'
        yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.delete_shipping', id=environment.getattr(l_1_method, 'id'), _loop_vars=_loop_vars))
        yield '" onsubmit="return confirm(\'Delete this shipping method?\');">\n          <button type="submit">Delete</button>\n        </form>\n      </td>\n    </tr>\n    '
        t_2 = 0
    l_1_method = l_1_config = missing
    if t_2:
        pass
        yield '\n    <tr class="empty-row"><td colspan="5">No shipping methods configured.</td></tr>\n    '
    yield '\n  </tbody>\n</table>\n'

blocks = {'content': block_content}
debug_info = '1=12&3=17&9=34&23=37&25=42&26=44&27=47&28=49&30=58'