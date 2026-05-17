from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'admin/category_form.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('admin/admin_base.html', 'admin/category_form.html')
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
    l_0_category = resolve('category')
    l_0_categories = resolve('categories')
    l_0_url_for = resolve('url_for')
    pass
    yield '\n<div class="page-header">\n  <div>\n    <h1 class="page-title">'
    if (undefined(name='category') if l_0_category is missing else l_0_category):
        pass
        yield 'Edit Category'
    else:
        pass
        yield 'Add Category'
    yield '</h1>\n  </div>\n</div>\n\n<div class="admin-form-card">\n  <form method="POST" style="display: flex; flex-direction: column; gap: 0;">\n    <div class="form-group">\n      <label class="form-label" for="name">Name *</label>\n      <input class="form-input" type="text" id="name" name="name" required value="'
    yield escape((environment.getattr((undefined(name='category') if l_0_category is missing else l_0_category), 'name') if (undefined(name='category') if l_0_category is missing else l_0_category) else ''))
    yield '">\n    </div>\n    <div class="form-group">\n      <label class="form-label" for="slug">Slug (auto-generated if blank)</label>\n      <input class="form-input" type="text" id="slug" name="slug" value="'
    yield escape((environment.getattr((undefined(name='category') if l_0_category is missing else l_0_category), 'slug') if (undefined(name='category') if l_0_category is missing else l_0_category) else ''))
    yield '">\n    </div>\n    <div class="form-group">\n      <label class="form-label" for="description">Description</label>\n      <textarea class="form-input" id="description" name="description" rows="3" style="resize: vertical; border: 1px solid rgba(201,168,76,0.15); padding: 0.6rem;">'
    yield escape((environment.getattr((undefined(name='category') if l_0_category is missing else l_0_category), 'description') if (undefined(name='category') if l_0_category is missing else l_0_category) else ''))
    yield '</textarea>\n    </div>\n    <div class="form-group">\n      <label class="form-label" for="parent_id">Parent Category</label>\n      <select class="form-select" id="parent_id" name="parent_id">\n        <option value="">— None (top level) —</option>\n        '
    for l_1_cat in (undefined(name='categories') if l_0_categories is missing else l_0_categories):
        _loop_vars = {}
        pass
        yield '\n          '
        if ((not (undefined(name='category') if l_0_category is missing else l_0_category)) or (environment.getattr(l_1_cat, 'id') != environment.getattr((undefined(name='category') if l_0_category is missing else l_0_category), 'id'))):
            pass
            yield '\n          <option value="'
            yield escape(environment.getattr(l_1_cat, 'id'))
            yield '" '
            if ((undefined(name='category') if l_0_category is missing else l_0_category) and (environment.getattr((undefined(name='category') if l_0_category is missing else l_0_category), 'parent_id') == environment.getattr(l_1_cat, 'id'))):
                pass
                yield 'selected'
            yield '>'
            yield escape(environment.getattr(l_1_cat, 'name'))
            yield '</option>\n          '
        yield '\n        '
    l_1_cat = missing
    yield '\n      </select>\n    </div>\n    <div class="form-group">\n      <label class="form-checkbox">\n        <input type="checkbox" name="is_featured" value="yes" '
    if ((undefined(name='category') if l_0_category is missing else l_0_category) and environment.getattr((undefined(name='category') if l_0_category is missing else l_0_category), 'is_featured')):
        pass
        yield 'checked'
    yield '>\n        Featured Category (shown as section on collection page)\n      </label>\n    </div>\n    <div class="form-actions">\n      <button type="submit" class="btn-admin-primary">Save</button>\n      <a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.manage_categories', _block_vars=_block_vars))
    yield '" class="btn-admin-secondary">Cancel</a>\n    </div>\n  </form>\n</div>\n'

blocks = {'content': block_content}
debug_info = '1=12&3=17&6=29&14=36&18=38&22=40&28=42&29=46&30=49&37=60&43=64'