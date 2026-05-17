from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'admin/variant_form.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('admin/admin_base.html', 'admin/variant_form.html')
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
    pass
    yield '\n<div class="page-header">\n  <div>\n    <h1 class="page-title">Add Variant</h1>\n    <div class="page-subtitle">For '
    yield escape(environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'name'))
    yield ' ('
    yield escape(environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'sku'))
    yield ')</div>\n  </div>\n</div>\n\n<div class="admin-form-card">\n  <form method="POST" style="display: flex; flex-direction: column; gap: 0;">\n\n    <div class="form-group">\n      <label class="form-label" for="sku">Variant SKU *</label>\n      <input class="form-input" type="text" id="sku" name="sku" required value="'
    yield escape(environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'sku'))
    yield '-V'
    yield escape((context.call(environment.getattr(environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'variants'), 'count'), _block_vars=_block_vars) + 1))
    yield '">\n    </div>\n\n    <div class="form-row">\n      <div class="form-group">\n        <label class="form-label" for="color">Color</label>\n        <input class="form-input" type="text" id="color" name="color" placeholder="e.g. Rose Gold">\n      </div>\n      <div class="form-group">\n        <label class="form-label" for="strap_type">Strap Type</label>\n        <input class="form-input" type="text" id="strap_type" name="strap_type" placeholder="e.g. Leather">\n      </div>\n    </div>\n\n    <div class="form-row">\n      <div class="form-group">\n        <label class="form-label" for="size">Size / Dial</label>\n        <input class="form-input" type="text" id="size" name="size" placeholder="e.g. 42mm">\n      </div>\n      <div class="form-group">\n        <label class="form-label" for="edition">Edition</label>\n        <input class="form-input" type="text" id="edition" name="edition" placeholder="e.g. Limited Edition">\n      </div>\n    </div>\n\n    <div class="form-row">\n      <div class="form-group">\n        <label class="form-label" for="price_override">Price Override ('
    yield escape(environment.getattr((undefined(name='config') if l_0_config is missing else l_0_config), 'CURRENCY_SYMBOL'))
    yield ')</label>\n        <input class="form-input" type="number" step="0.01" id="price_override" name="price_override" placeholder="Leave blank for base price">\n      </div>\n      <div class="form-group">\n        <label class="form-label" for="quantity">Quantity in Stock *</label>\n        <input class="form-input" type="number" id="quantity" name="quantity" required value="0">\n      </div>\n    </div>\n\n    <div class="form-actions">\n      <button type="submit" class="btn-admin-primary">Forge Variant</button>\n      <a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.manage_product_variants', id=environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'id'), _block_vars=_block_vars))
    yield '" class="btn-admin-secondary">Cancel</a>\n    </div>\n  </form>\n</div>\n'

blocks = {'content': block_content}
debug_info = '1=12&3=17&7=29&16=33&43=37&54=39'