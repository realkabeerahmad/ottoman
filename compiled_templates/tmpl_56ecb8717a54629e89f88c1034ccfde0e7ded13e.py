from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'admin/payment_methods.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('admin/admin_base.html', 'admin/payment_methods.html')
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
    pass
    yield '\n<div class="page-header">\n  <div>\n    <h1 class="page-title">Payment Methods</h1>\n    <div class="page-subtitle">Configure accepted payment options</div>\n  </div>\n  <a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.add_payment_method', _block_vars=_block_vars))
    yield '" class="btn-admin-primary">+ Add Method</a>\n</div>\n\n<table class="data-table">\n  <thead>\n    <tr>\n      <th>Name</th>\n      <th>Instructions</th>\n      <th>Active</th>\n      <th>Actions</th>\n    </tr>\n  </thead>\n  <tbody>\n    '
    t_1 = 1
    for l_1_method in (undefined(name='methods') if l_0_methods is missing else l_0_methods):
        _loop_vars = {}
        pass
        yield '\n    <tr>\n      <td>'
        yield escape(environment.getattr(l_1_method, 'name'))
        yield '</td>\n      <td class="muted">'
        yield escape((environment.getattr(l_1_method, 'instructions') or '—'))
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
        yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.delete_payment_method', id=environment.getattr(l_1_method, 'id'), _loop_vars=_loop_vars))
        yield '" onsubmit="return confirm(\'Delete this payment method?\');">\n          <button type="submit">Delete</button>\n        </form>\n      </td>\n    </tr>\n    '
        t_1 = 0
    l_1_method = missing
    if t_1:
        pass
        yield '\n    <tr class="empty-row"><td colspan="4">No payment methods configured.</td></tr>\n    '
    yield '\n  </tbody>\n</table>\n'

blocks = {'content': block_content}
debug_info = '1=12&3=17&9=28&22=31&24=35&25=37&26=39&28=48'