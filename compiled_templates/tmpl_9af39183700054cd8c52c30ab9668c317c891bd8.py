from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'admin/payment_form.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('admin/admin_base.html', 'admin/payment_form.html')
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
    pass
    yield '\n<div class="page-header">\n  <div>\n    <h1 class="page-title">Add Payment Method</h1>\n  </div>\n</div>\n\n<div class="admin-form-card">\n  <form method="POST" style="display: flex; flex-direction: column; gap: 0;">\n    <div class="form-group">\n      <label class="form-label" for="name">Name *</label>\n      <input class="form-input" type="text" id="name" name="name" required placeholder="e.g. Cash on Delivery">\n    </div>\n    <div class="form-group">\n      <label class="form-label" for="instructions">Instructions for Customer</label>\n      <textarea class="form-input" id="instructions" name="instructions" rows="3" style="resize: vertical; border: 1px solid rgba(201,168,76,0.15); padding: 0.6rem;" placeholder="e.g. Please keep exact change ready at the time of delivery."></textarea>\n    </div>\n    <div class="form-actions">\n      <button type="submit" class="btn-admin-primary">Save</button>\n      <a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.manage_payment_methods', _block_vars=_block_vars))
    yield '" class="btn-admin-secondary">Cancel</a>\n    </div>\n  </form>\n</div>\n'

blocks = {'content': block_content}
debug_info = '1=12&3=17&22=27'