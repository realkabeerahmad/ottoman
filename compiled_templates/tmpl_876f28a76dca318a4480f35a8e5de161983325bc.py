from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'admin/coupon_form.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('admin/admin_base.html', 'admin/coupon_form.html')
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
    yield '\n<div class="page-header">\n  <div>\n    <h1 class="page-title">Add Coupon</h1>\n  </div>\n</div>\n\n<div class="admin-form-card">\n  <form method="POST" style="display: flex; flex-direction: column; gap: 0;">\n    <div class="form-group">\n      <label class="form-label" for="code">Coupon Code *</label>\n      <input class="form-input" type="text" id="code" name="code" required style="text-transform: uppercase;">\n    </div>\n    <div class="form-row">\n      <div class="form-group">\n        <label class="form-label" for="discount_type">Discount Type</label>\n        <select class="form-select" id="discount_type" name="discount_type">\n          <option value="percentage">Percentage (%)</option>\n          <option value="fixed">Fixed Amount</option>\n        </select>\n      </div>\n      <div class="form-group">\n        <label class="form-label" for="discount_value">Discount Value *</label>\n        <input class="form-input" type="number" step="0.01" id="discount_value" name="discount_value" required>\n      </div>\n    </div>\n    <div class="form-group">\n      <label class="form-label" for="usage_limit">Usage Limit (leave blank for unlimited)</label>\n      <input class="form-input" type="number" id="usage_limit" name="usage_limit">\n    </div>\n    <div class="form-actions">\n      <button type="submit" class="btn-admin-primary">Create Coupon</button>\n      <a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.manage_coupons', _block_vars=_block_vars))
    yield '" class="btn-admin-secondary">Cancel</a>\n    </div>\n  </form>\n</div>\n'

blocks = {'content': block_content}
debug_info = '1=12&3=17&35=27'