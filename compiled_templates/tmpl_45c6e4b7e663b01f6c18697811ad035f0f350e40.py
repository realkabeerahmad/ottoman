from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'admin/order_statuses.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('admin/admin_base.html', 'admin/order_statuses.html')
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
    l_0_statuses = resolve('statuses')
    pass
    yield '\n<div class="page-header">\n  <div>\n    <h1 class="page-title">Order Statuses</h1>\n    <div class="page-subtitle">Configure order lifecycle stages</div>\n  </div>\n  <a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.add_order_status', _block_vars=_block_vars))
    yield '" class="btn-admin-primary">+ Add Status</a>\n</div>\n\n<table class="data-table">\n  <thead>\n    <tr>\n      <th>Name</th>\n      <th>Description</th>\n      <th>Actions</th>\n    </tr>\n  </thead>\n  <tbody>\n    '
    t_1 = 1
    for l_1_status in (undefined(name='statuses') if l_0_statuses is missing else l_0_statuses):
        _loop_vars = {}
        pass
        yield '\n    <tr>\n      <td>\n        '
        yield escape(environment.getattr(l_1_status, 'name'))
        yield '\n        '
        if environment.getattr(l_1_status, 'is_system'):
            pass
            yield '<span class="badge" style="background: rgba(201,168,76,0.15); color: var(--gold); font-size: 0.6rem; padding: 0.15rem 0.5rem; margin-left: 0.5rem;">🔒 System</span>'
        yield '\n        '
        if environment.getattr(l_1_status, 'is_default'):
            pass
            yield '<span class="badge" style="background: rgba(39,174,96,0.15); color: #27ae60; font-size: 0.6rem; padding: 0.15rem 0.5rem; margin-left: 0.3rem;">Default</span>'
        yield '\n      </td>\n      <td class="muted">'
        yield escape((environment.getattr(l_1_status, 'description') or '—'))
        yield '</td>\n      <td>\n        '
        if environment.getattr(l_1_status, 'is_system'):
            pass
            yield '\n          <span style="color: var(--text-dim); font-size: 0.75rem; font-style: italic;">Protected</span>\n        '
        else:
            pass
            yield '\n        <form class="delete-form" method="POST" action="'
            yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.delete_order_status', id=environment.getattr(l_1_status, 'id'), _loop_vars=_loop_vars))
            yield '" onsubmit="return confirm(\'Delete this status?\');">\n          <button type="submit">Delete</button>\n        </form>\n        '
        yield '\n      </td>\n    </tr>\n    '
        t_1 = 0
    l_1_status = missing
    if t_1:
        pass
        yield '\n    <tr class="empty-row"><td colspan="3">No order statuses configured.</td></tr>\n    '
    yield '\n  </tbody>\n</table>\n'

blocks = {'content': block_content}
debug_info = '1=12&3=17&9=28&21=31&24=35&25=37&26=41&28=45&30=47&33=53'