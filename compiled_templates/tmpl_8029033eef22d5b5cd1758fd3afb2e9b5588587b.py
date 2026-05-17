from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'admin/products.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('admin/admin_base.html', 'admin/products.html')
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
    l_0_products = resolve('products')
    try:
        t_1 = environment.filters['format']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'format' found.")
    pass
    yield '\n<div class="page-header">\n  <div>\n    <h1 class="page-title">Products</h1>\n    <div class="page-subtitle">Manage your catalog of timepieces</div>\n  </div>\n  <a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.add_product', _block_vars=_block_vars))
    yield '" class="btn-admin-primary">+ Add Timepiece</a>\n</div>\n\n<table class="data-table">\n  <thead>\n    <tr>\n      <th>SKU</th>\n      <th>Name</th>\n      <th>Category</th>\n      <th>Price</th>\n      <th>Stock</th>\n      <th>Status</th>\n      <th>Actions</th>\n    </tr>\n  </thead>\n  <tbody>\n    '
    t_2 = 1
    for l_1_product in (undefined(name='products') if l_0_products is missing else l_0_products):
        l_1_config = resolve('config')
        _loop_vars = {}
        pass
        yield '\n    <tr>\n      <td class="mono muted">'
        yield escape(environment.getattr(l_1_product, 'sku'))
        yield '</td>\n      <td>'
        yield escape(environment.getattr(l_1_product, 'name'))
        if environment.getattr(l_1_product, 'is_featured'):
            pass
            yield ' <span class="badge badge-active">Featured</span>'
        yield '</td>\n      <td class="muted">'
        yield escape((environment.getattr(environment.getattr(l_1_product, 'category'), 'name') if environment.getattr(l_1_product, 'category') else '—'))
        yield '</td>\n      <td class="gold">\n        '
        yield escape(environment.getattr((undefined(name='config') if l_1_config is missing else l_1_config), 'CURRENCY_SYMBOL'))
        yield escape(t_1('%.2f', environment.getattr(l_1_product, 'price')))
        yield '\n        '
        if environment.getattr(l_1_product, 'discount_price'):
            pass
            yield '\n          <br><small class="muted" style="text-decoration: line-through;">'
            yield escape(environment.getattr((undefined(name='config') if l_1_config is missing else l_1_config), 'CURRENCY_SYMBOL'))
            yield escape(t_1('%.2f', environment.getattr(l_1_product, 'discount_price')))
            yield '</small>\n        '
        yield '\n      </td>\n      <td>\n        '
        if (environment.getattr(l_1_product, 'stock_status') == 'in_stock'):
            pass
            yield '<span class="badge badge-active">In Stock</span>\n        '
        elif (environment.getattr(l_1_product, 'stock_status') == 'out_of_stock'):
            pass
            yield '<span class="badge badge-inactive">Out of Stock</span>\n        '
        else:
            pass
            yield '<span class="badge badge-warning">Pre-order</span>'
        yield '\n      </td>\n      <td><span class="badge '
        if (environment.getattr(l_1_product, 'status') == 'active'):
            pass
            yield 'badge-active'
        else:
            pass
            yield 'badge-inactive'
        yield '">'
        yield escape(environment.getattr(l_1_product, 'status'))
        yield '</span></td>\n      <td>\n        <a href="'
        yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.manage_product_variants', id=environment.getattr(l_1_product, 'id'), _loop_vars=_loop_vars))
        yield '" class="action-link manage">Variants</a>\n        <a href="'
        yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.edit_product', id=environment.getattr(l_1_product, 'id'), _loop_vars=_loop_vars))
        yield '" class="action-link edit">Edit</a>\n        <form class="delete-form" method="POST" action="'
        yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.delete_product', id=environment.getattr(l_1_product, 'id'), _loop_vars=_loop_vars))
        yield '" onsubmit="return confirm(\'Delete this timepiece?\');">\n          <button type="submit">Delete</button>\n        </form>\n      </td>\n    </tr>\n    '
        t_2 = 0
    l_1_product = l_1_config = missing
    if t_2:
        pass
        yield '\n    <tr class="empty-row"><td colspan="7">No timepieces found. Forge your first creation.</td></tr>\n    '
    yield '\n  </tbody>\n</table>\n'

blocks = {'content': block_content}
debug_info = '1=12&3=17&9=34&25=37&27=42&28=44&29=49&31=51&32=54&33=57&37=61&38=64&41=71&43=80&44=82&45=84'