from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'admin/product_form.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('admin/admin_base.html', 'admin/product_form.html')
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
    l_0_categories = resolve('categories')
    l_0_url_for = resolve('url_for')
    pass
    yield '\n<div class="page-header">\n  <div>\n    <h1 class="page-title">'
    if (undefined(name='product') if l_0_product is missing else l_0_product):
        pass
        yield 'Edit Timepiece'
    else:
        pass
        yield 'Forge Timepiece'
    yield '</h1>\n    <div class="page-subtitle">'
    if (undefined(name='product') if l_0_product is missing else l_0_product):
        pass
        yield 'Updating '
        yield escape(environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'name'))
    else:
        pass
        yield 'Add a new creation to the catalog'
    yield '</div>\n  </div>\n</div>\n\n<div class="admin-form-card">\n  <form method="POST" enctype="multipart/form-data" style="display: flex; flex-direction: column; gap: 0;">\n\n    <div class="form-row">\n      <div class="form-group">\n        <label class="form-label" for="name">Name *</label>\n        <input class="form-input" type="text" id="name" name="name" required value="'
    yield escape((environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'name') if (undefined(name='product') if l_0_product is missing else l_0_product) else ''))
    yield '">\n      </div>\n      <div class="form-group">\n        <label class="form-label" for="sku">SKU *</label>\n        <input class="form-input" type="text" id="sku" name="sku" required value="'
    yield escape((environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'sku') if (undefined(name='product') if l_0_product is missing else l_0_product) else ''))
    yield '">\n      </div>\n    </div>\n\n    <div class="form-row">\n      <div class="form-group">\n        <label class="form-label" for="price">Price ('
    yield escape(environment.getattr((undefined(name='config') if l_0_config is missing else l_0_config), 'CURRENCY_SYMBOL'))
    yield ') *</label>\n        <input class="form-input" type="number" step="0.01" id="price" name="price" required value="'
    yield escape((environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'price') if (undefined(name='product') if l_0_product is missing else l_0_product) else ''))
    yield '">\n      </div>\n      <div class="form-group">\n        <label class="form-label" for="discount_price">Discount Price</label>\n        <input class="form-input" type="number" step="0.01" id="discount_price" name="discount_price" value="'
    yield escape((environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'discount_price') if ((undefined(name='product') if l_0_product is missing else l_0_product) and environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'discount_price')) else ''))
    yield '">\n      </div>\n    </div>\n\n    <div class="form-row">\n      <div class="form-group">\n        <label class="form-label" for="category_id">Category</label>\n        <select class="form-select" id="category_id" name="category_id">\n          <option value="">— None —</option>\n          '
    for l_1_cat in (undefined(name='categories') if l_0_categories is missing else l_0_categories):
        _loop_vars = {}
        pass
        yield '\n          <option value="'
        yield escape(environment.getattr(l_1_cat, 'id'))
        yield '" '
        if ((undefined(name='product') if l_0_product is missing else l_0_product) and (environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'category_id') == environment.getattr(l_1_cat, 'id'))):
            pass
            yield 'selected'
        yield '>'
        yield escape(environment.getattr(l_1_cat, 'name'))
        yield '</option>\n          '
    l_1_cat = missing
    yield '\n        </select>\n      </div>\n      <div class="form-group">\n        <label class="form-label" for="stock_status">Stock Status</label>\n        <select class="form-select" id="stock_status" name="stock_status">\n          <option value="in_stock" '
    if ((undefined(name='product') if l_0_product is missing else l_0_product) and (environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'stock_status') == 'in_stock')):
        pass
        yield 'selected'
    yield '>In Stock</option>\n          <option value="out_of_stock" '
    if ((undefined(name='product') if l_0_product is missing else l_0_product) and (environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'stock_status') == 'out_of_stock')):
        pass
        yield 'selected'
    yield '>Out of Stock</option>\n          <option value="pre_order" '
    if ((undefined(name='product') if l_0_product is missing else l_0_product) and (environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'stock_status') == 'pre_order')):
        pass
        yield 'selected'
    yield '>Pre-order</option>\n        </select>\n      </div>\n    </div>\n\n    <div class="form-group">\n      <label class="form-checkbox">\n        <input type="checkbox" name="is_featured" value="yes" '
    if ((undefined(name='product') if l_0_product is missing else l_0_product) and environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'is_featured')):
        pass
        yield 'checked'
    yield '>\n        Featured Timepiece (shown on homepage)\n      </label>\n    </div>\n\n    <div class="form-group">\n      <label class="form-label" for="short_description">Short Description</label>\n      <input class="form-input" type="text" id="short_description" name="short_description" value="'
    yield escape((environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'short_description') if (undefined(name='product') if l_0_product is missing else l_0_product) else ''))
    yield '">\n    </div>\n\n    <div class="form-group">\n      <label class="form-label" for="description">Full Description</label>\n      <textarea class="form-input" id="description" name="description" rows="4" style="resize: vertical; border: 1px solid rgba(201,168,76,0.15); padding: 0.6rem;">'
    yield escape((environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'description') if (undefined(name='product') if l_0_product is missing else l_0_product) else ''))
    yield '</textarea>\n    </div>\n\n    <div class="form-group">\n      <label class="form-label" for="main_image">Product Image</label>\n      '
    if ((undefined(name='product') if l_0_product is missing else l_0_product) and environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'main_image')):
        pass
        yield '\n      <div style="margin-bottom: 0.8rem;">\n        <img src="'
        yield escape(environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'main_image'))
        yield '" alt="Current" style="width: 120px; height: 120px; object-fit: cover; border: 1px solid rgba(201,168,76,0.15);">\n        <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 0.3rem;">Current image — upload new to replace</div>\n      </div>\n      '
    yield '\n      <input type="file" id="main_image" name="main_image" accept="image/*" style="color: rgba(255,255,255,0.6); font-family: \'Cormorant Garamond\', serif;">\n    </div>\n\n    <div class="form-actions">\n      <button type="submit" class="btn-admin-primary">'
    if (undefined(name='product') if l_0_product is missing else l_0_product):
        pass
        yield 'Update'
    else:
        pass
        yield 'Forge'
    yield '</button>\n      <a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.manage_products', _block_vars=_block_vars))
    yield '" class="btn-admin-secondary">Cancel</a>\n    </div>\n  </form>\n</div>\n'

blocks = {'content': block_content}
debug_info = '1=12&3=17&6=30&7=37&17=45&21=47&27=49&28=51&32=53&41=55&42=59&49=69&50=73&51=77&58=81&65=85&70=87&75=89&77=92&85=95&86=102'