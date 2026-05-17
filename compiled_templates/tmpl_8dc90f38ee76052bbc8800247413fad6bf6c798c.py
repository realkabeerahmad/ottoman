from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'admin/categories.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('admin/admin_base.html', 'admin/categories.html')
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
    l_0_categories = resolve('categories')
    pass
    yield '\n<div class="page-header">\n  <div>\n    <h1 class="page-title">Categories</h1>\n    <div class="page-subtitle">Organize your collection</div>\n  </div>\n  <a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.add_category', _block_vars=_block_vars))
    yield '" class="btn-admin-primary">+ Add Category</a>\n</div>\n\n<table class="data-table">\n  <thead>\n    <tr>\n      <th>Name</th>\n      <th>Slug</th>\n      <th>Parent</th>\n      <th>Status</th>\n      <th>Actions</th>\n    </tr>\n  </thead>\n  <tbody>\n    '
    t_1 = 1
    for l_1_category in (undefined(name='categories') if l_0_categories is missing else l_0_categories):
        _loop_vars = {}
        pass
        yield '\n    <tr>\n      <td>'
        yield escape(environment.getattr(l_1_category, 'name'))
        yield '</td>\n      <td class="mono muted">'
        yield escape(environment.getattr(l_1_category, 'slug'))
        yield '</td>\n      <td class="muted">'
        yield escape((environment.getattr(environment.getattr(l_1_category, 'parent'), 'name') if environment.getattr(l_1_category, 'parent') else '—'))
        yield '</td>\n      <td><span class="badge '
        if (environment.getattr(l_1_category, 'status') == 'active'):
            pass
            yield 'badge-active'
        else:
            pass
            yield 'badge-inactive'
        yield '">'
        yield escape(environment.getattr(l_1_category, 'status'))
        yield '</span></td>\n      <td>\n        <a href="'
        yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.edit_category', id=environment.getattr(l_1_category, 'id'), _loop_vars=_loop_vars))
        yield '" class="action-link edit">Edit</a>\n        <form class="delete-form" method="POST" action="'
        yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.delete_category', id=environment.getattr(l_1_category, 'id'), _loop_vars=_loop_vars))
        yield '" onsubmit="return confirm(\'Delete this category?\');">\n          <button type="submit">Delete</button>\n        </form>\n      </td>\n    </tr>\n    '
        t_1 = 0
    l_1_category = missing
    if t_1:
        pass
        yield '\n    <tr class="empty-row"><td colspan="5">No categories found.</td></tr>\n    '
    yield '\n  </tbody>\n</table>\n'

blocks = {'content': block_content}
debug_info = '1=12&3=17&9=28&23=31&25=35&26=37&27=39&28=41&30=50&31=52'