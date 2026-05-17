from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'admin/product_manage.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('admin/admin_base.html', 'admin/product_manage.html')
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
    l_0_product = resolve('product')
    l_0_config = resolve('config')
    l_0_url_for = resolve('url_for')
    try:
        t_1 = environment.filters['format']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'format' found.")
    pass
    yield '\n<div class="page-header">\n  <div>\n    <h1 class="page-title">'
    yield escape(environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'name'))
    yield '</h1>\n    <div class="page-subtitle">SKU: '
    yield escape(environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'sku'))
    yield ' · Base Price: '
    yield escape(environment.getattr((undefined(name='config') if l_0_config is missing else l_0_config), 'CURRENCY_SYMBOL'))
    yield escape(t_1('%.2f', environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'price')))
    yield '</div>\n  </div>\n  <a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.add_product_variant', id=environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'id'), _block_vars=_block_vars))
    yield '" class="btn-admin-primary">+ Add Variant</a>\n</div>\n\n<table class="data-table">\n  <thead>\n    <tr>\n      <th>Variant SKU</th>\n      <th>Color</th>\n      <th>Strap</th>\n      <th>Size</th>\n      <th>Edition</th>\n      <th>Price</th>\n      <th>Quantity</th>\n      <th>Actions</th>\n    </tr>\n  </thead>\n  <tbody>\n    '
    t_2 = 1
    for l_1_variant in environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'variants'):
        _loop_vars = {}
        pass
        yield '\n    <tr>\n      <td class="mono">'
        yield escape(environment.getattr(l_1_variant, 'sku'))
        yield '</td>\n      <td>'
        yield escape((environment.getattr(l_1_variant, 'color') or '—'))
        yield '</td>\n      <td>'
        yield escape((environment.getattr(l_1_variant, 'strap_type') or '—'))
        yield '</td>\n      <td>'
        yield escape((environment.getattr(l_1_variant, 'size') or '—'))
        yield '</td>\n      <td class="muted">'
        yield escape((environment.getattr(l_1_variant, 'edition') or '—'))
        yield '</td>\n      <td class="gold">\n        '
        if environment.getattr(l_1_variant, 'price_override'):
            pass
            yield '\n          '
            yield escape(environment.getattr((undefined(name='config') if l_0_config is missing else l_0_config), 'CURRENCY_SYMBOL'))
            yield escape(t_1('%.2f', environment.getattr(l_1_variant, 'price_override')))
            yield '\n        '
        else:
            pass
            yield '\n          Base\n        '
        yield '\n      </td>\n      <td style="font-weight: bold; color: '
        if (environment.getattr(l_1_variant, 'quantity') == 0):
            pass
            yield '#e74c3c'
        elif (environment.getattr(l_1_variant, 'quantity') <= 5):
            pass
            yield '#f39c12'
        else:
            pass
            yield 'var(--gold)'
        yield ';">\n        '
        yield escape(environment.getattr(l_1_variant, 'quantity'))
        yield '\n      </td>\n      <td>\n        <form class="delete-form" method="POST" action="'
        yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.delete_product_variant', id=environment.getattr(l_1_variant, 'id'), _loop_vars=_loop_vars))
        yield '" onsubmit="return confirm(\'Delete this variant?\');">\n          <button type="submit">Delete</button>\n        </form>\n      </td>\n    </tr>\n    '
        t_2 = 0
    l_1_variant = missing
    if t_2:
        pass
        yield '\n    <tr class="empty-row"><td colspan="8">No variants configured. Product uses base configuration only.</td></tr>\n    '
    yield '\n  </tbody>\n</table>\n'

blocks = {'content': block_content}
debug_info = '1=12&3=17&6=35&7=37&9=42&26=45&28=49&29=51&30=53&31=55&32=57&34=59&35=62&40=69&41=79&44=81'