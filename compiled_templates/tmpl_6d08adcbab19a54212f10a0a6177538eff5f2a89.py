from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'shop/product_detail.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('base.html', 'shop/product_detail.html')
    for name, parent_block in parent_template.blocks.items():
        context.blocks.setdefault(name, []).append(parent_block)
    yield from parent_template.root_render_func(context)

def block_title(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    _block_vars = {}
    l_0_product = resolve('product')
    pass
    yield escape(environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'name'))
    yield ' — Ottoman Time'

def block_content(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    _block_vars = {}
    l_0_url_for = resolve('url_for')
    l_0_product = resolve('product')
    l_0_config = resolve('config')
    l_0_related = resolve('related')
    try:
        t_1 = environment.filters['format']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'format' found.")
    pass
    yield '\n<section class="detail-section" style="padding: 120px 4rem 6rem; max-width: 1200px; margin: 0 auto;">\n\n  <!-- Breadcrumb -->\n  <div style="font-family: \'Cinzel\', serif; font-size: 0.65rem; letter-spacing: 0.2em; text-transform: uppercase; color: var(--text-dim); margin-bottom: 3rem;">\n    <a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'shop.collection', _block_vars=_block_vars))
    yield '" style="color: var(--text-muted); text-decoration: none;">Collection</a>\n    <span style="margin: 0 0.8rem;">→</span>\n    '
    if environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'category'):
        pass
        yield '\n    <a href="'
        yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'shop.collection', _block_vars=_block_vars))
        yield '" style="color: var(--text-muted); text-decoration: none;">'
        yield escape(environment.getattr(environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'category'), 'name'))
        yield '</a>\n    <span style="margin: 0 0.8rem;">→</span>\n    '
    yield '\n    <span style="color: var(--gold);">'
    yield escape(environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'name'))
    yield '</span>\n  </div>\n\n  <div class="detail-grid">\n    \n    <!-- Product Image -->\n    <div class="detail-image reveal" data-reveal-delay="0">\n      '
    if environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'main_image'):
        pass
        yield '\n        <img src="'
        yield escape(environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'main_image'))
        yield '" alt="'
        yield escape(environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'name'))
        yield '" style="width: 100%; height: 100%; object-fit: cover;">\n      '
    else:
        pass
        yield '\n        <div style="text-align: center; color: var(--text-dim);">\n          <div style="font-size: 4rem; margin-bottom: 1rem;">⌚</div>\n          <div style="font-family: \'Cinzel\', serif; font-size: 0.7rem; letter-spacing: 0.2em; text-transform: uppercase;">No image</div>\n        </div>\n      '
    yield '\n      '
    if environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'is_featured'):
        pass
        yield '\n      <span class="product-badge">Signature</span>\n      '
    yield '\n      '
    if environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'discount_price'):
        pass
        yield '\n      <span style="position: absolute; top: 1rem; left: 1rem; background: #c0392b; color: white; font-family: \'Cinzel\', serif; font-size: 0.55rem; letter-spacing: 0.1em; padding: 0.3rem 0.7rem; text-transform: uppercase; font-weight: 700;">Sale</span>\n      '
    yield '\n    </div>\n\n    <!-- Product Info -->\n    <div class="reveal" data-reveal-delay="150">\n      '
    if environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'category'):
        pass
        yield '\n      <span style="font-family: \'Cinzel\', serif; font-size: 0.6rem; letter-spacing: 0.3em; color: var(--gold); text-transform: uppercase; display: block; margin-bottom: 0.8rem;">'
        yield escape(environment.getattr(environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'category'), 'name'))
        yield ' Collection</span>\n      '
    yield '\n\n      <h1 style="font-family: \'Cinzel Decorative\', serif; font-size: 2.4rem; color: var(--text-primary); line-height: 1.2; margin-bottom: 1rem;">'
    yield escape(environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'name'))
    yield '</h1>\n      \n      '
    if environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'short_description'):
        pass
        yield '\n      <p style="font-style: italic; color: var(--text-muted); font-size: 1.1rem; line-height: 1.7; margin-bottom: 2rem;">'
        yield escape(environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'short_description'))
        yield '</p>\n      '
    yield '\n\n      <!-- Price -->\n      <div style="margin-bottom: 2rem; padding-bottom: 2rem; border-bottom: 1px solid var(--glass-border);">\n        '
    if environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'discount_price'):
        pass
        yield '\n          <div style="font-family: \'Cinzel Decorative\', serif; font-size: 2.5rem; color: var(--gold);">\n            '
        yield escape(environment.getattr((undefined(name='config') if l_0_config is missing else l_0_config), 'CURRENCY_SYMBOL'))
        yield escape(t_1('%.0f', environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'discount_price')))
        yield '\n          </div>\n          <div style="font-family: \'Cinzel\', serif; font-size: 1.1rem; color: var(--text-dim); text-decoration: line-through; margin-top: 0.3rem;">\n            '
        yield escape(environment.getattr((undefined(name='config') if l_0_config is missing else l_0_config), 'CURRENCY_SYMBOL'))
        yield escape(t_1('%.0f', environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'price')))
        yield '\n          </div>\n          <div style="font-family: \'Cinzel\', serif; font-size: 0.7rem; color: #27ae60; letter-spacing: 0.1em; margin-top: 0.3rem;">\n            SAVE '
        yield escape(environment.getattr((undefined(name='config') if l_0_config is missing else l_0_config), 'CURRENCY_SYMBOL'))
        yield escape(t_1('%.0f', (environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'price') - environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'discount_price'))))
        yield '\n          </div>\n        '
    else:
        pass
        yield '\n          <div style="font-family: \'Cinzel Decorative\', serif; font-size: 2.5rem; color: var(--gold);">\n            '
        yield escape(environment.getattr((undefined(name='config') if l_0_config is missing else l_0_config), 'CURRENCY_SYMBOL'))
        yield escape(t_1('%.0f', environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'price')))
        yield '\n          </div>\n        '
    yield '\n      </div>\n\n      <!-- SKU & Status -->\n      <div style="display: flex; gap: 2rem; margin-bottom: 2rem; font-family: \'Cinzel\', serif; font-size: 0.7rem; letter-spacing: 0.1em; text-transform: uppercase;">\n        <span style="color: var(--text-dim);"><i data-lucide="tag" style="width:12px;height:12px;margin-right:0.3rem;vertical-align:-2px;"></i>SKU: '
    yield escape(environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'sku'))
    yield '</span>\n        <span style="color: '
    if (environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'stock_status') == 'in_stock'):
        pass
        yield '#27ae60'
    elif (environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'stock_status') == 'out_of_stock'):
        pass
        yield '#c0392b'
    else:
        pass
        yield '#f39c12'
    yield ';">\n          '
    if (environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'stock_status') == 'in_stock'):
        pass
        yield '<i data-lucide="check-circle" style="width:12px;height:12px;margin-right:0.3rem;vertical-align:-2px;"></i>In Stock'
    elif (environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'stock_status') == 'out_of_stock'):
        pass
        yield '<i data-lucide="x-circle" style="width:12px;height:12px;margin-right:0.3rem;vertical-align:-2px;"></i>Out of Stock'
    else:
        pass
        yield '<i data-lucide="clock" style="width:12px;height:12px;margin-right:0.3rem;vertical-align:-2px;"></i>Pre-order'
    yield '\n        </span>\n      </div>\n\n      <!-- Variants -->\n      '
    if (context.call(environment.getattr(environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'variants'), 'count'), _block_vars=_block_vars) > 0):
        pass
        yield '\n      <div style="margin-bottom: 2rem;">\n        <div style="font-family: \'Cinzel\', serif; font-size: 0.7rem; letter-spacing: 0.2em; text-transform: uppercase; color: var(--text-muted); margin-bottom: 0.8rem;">Available Variants</div>\n        '
        for l_1_variant in environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'variants'):
            _loop_vars = {}
            pass
            yield '\n        <div style="display: inline-block; padding: 0.4rem 1rem; margin: 0 0.3rem 0.3rem 0; border: 1px solid var(--glass-border); font-family: \'Cinzel\', serif; font-size: 0.7rem; color: var(--text-primary); letter-spacing: 0.05em;">\n          '
            yield escape((environment.getattr(l_1_variant, 'color') or ''))
            yield ' '
            yield escape((environment.getattr(l_1_variant, 'strap_type') or ''))
            yield ' '
            yield escape((environment.getattr(l_1_variant, 'size') or ''))
            yield '\n          '
            if environment.getattr(l_1_variant, 'price_override'):
                pass
                yield ' · '
                yield escape(environment.getattr((undefined(name='config') if l_0_config is missing else l_0_config), 'CURRENCY_SYMBOL'))
                yield escape(t_1('%.0f', environment.getattr(l_1_variant, 'price_override')))
            yield '\n          '
            if (environment.getattr(l_1_variant, 'quantity') <= 0):
                pass
                yield ' <span style="color: #c0392b;">(Sold Out)</span>'
            yield '\n        </div>\n        '
        l_1_variant = missing
        yield '\n      </div>\n      '
    yield '\n\n      <!-- Add to Cart -->\n      '
    if (environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'stock_status') != 'out_of_stock'):
        pass
        yield '\n      <button class="btn-primary" onclick="event.stopPropagation(); addToCart('
        yield escape(environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'id'))
        yield ')" style="width: 100%; padding: 1.2rem; font-size: 0.8rem;">\n        <i data-lucide="shopping-bag" style="width:14px;height:14px;margin-right:0.4rem;vertical-align:-2px;"></i>Add to Collection\n      </button>\n      '
    else:
        pass
        yield '\n      <button class="btn-secondary" style="width: 100%; padding: 1.2rem; font-size: 0.8rem; cursor: not-allowed; opacity: 0.5;" disabled>\n        <i data-lucide="slash" style="width:14px;height:14px;margin-right:0.4rem;vertical-align:-2px;"></i>Currently Unavailable\n      </button>\n      '
    yield '\n\n      <!-- Description -->\n      '
    if environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'description'):
        pass
        yield '\n      <div style="margin-top: 3rem; padding-top: 2rem; border-top: 1px solid var(--glass-border);">\n        <div style="font-family: \'Cinzel\', serif; font-size: 0.7rem; letter-spacing: 0.2em; text-transform: uppercase; color: var(--gold); margin-bottom: 1rem;">About This Timepiece</div>\n        <div style="color: var(--text-muted); line-height: 1.8; font-size: 1.05rem;">'
        yield escape(environment.getattr((undefined(name='product') if l_0_product is missing else l_0_product), 'description'))
        yield '</div>\n      </div>\n      '
    yield '\n    </div>\n  </div>\n\n  <!-- Related Products -->\n  '
    if (undefined(name='related') if l_0_related is missing else l_0_related):
        pass
        yield '\n  <div style="margin-top: 6rem;">\n    <div class="section-header reveal">\n      <span class="section-label"><i data-lucide="compass" style="width:14px;height:14px;margin-right:0.3rem;vertical-align:-2px;"></i> You May Also Appreciate <i data-lucide="compass" style="width:14px;height:14px;margin-left:0.3rem;vertical-align:-2px;"></i></span>\n    </div>\n    <div class="products-grid" style="max-width: 1200px; margin: 0 auto;">\n      '
        l_1_loop = missing
        for l_1_p, l_1_loop in LoopContext((undefined(name='related') if l_0_related is missing else l_0_related), undefined):
            _loop_vars = {}
            pass
            yield '\n      <div class="product-card reveal" data-reveal-delay="'
            yield escape((environment.getattr(l_1_loop, 'index0') * 100))
            yield '" onclick="window.location.href=\''
            yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'shop.product_detail', slug=environment.getattr(l_1_p, 'slug'), _loop_vars=_loop_vars))
            yield '\'">\n        '
            if environment.getattr(l_1_p, 'is_featured'):
                pass
                yield '\n        <span class="product-badge">Featured</span>\n        '
            yield '\n        <div class="product-img">\n          <div class="watch-illustration" style="'
            if environment.getattr(l_1_p, 'main_image'):
                pass
                yield "background-image: url('"
                yield escape(environment.getattr(l_1_p, 'main_image'))
                yield "'); background-size: cover;"
            yield '"></div>\n        </div>\n        <div class="product-info">\n          <span class="product-collection-tag">'
            yield escape((environment.getattr(environment.getattr(l_1_p, 'category'), 'name') if environment.getattr(l_1_p, 'category') else 'Ottoman Time'))
            yield '</span>\n          <h3 class="product-name">'
            yield escape(environment.getattr(l_1_p, 'name'))
            yield '</h3>\n          <p class="product-desc">'
            yield escape((environment.getattr(l_1_p, 'short_description') or ''))
            yield '</p>\n          <div class="product-footer">\n            '
            if environment.getattr(l_1_p, 'discount_price'):
                pass
                yield '\n              <span class="product-price">\n                <span class="currency">'
                yield escape(environment.getattr((undefined(name='config') if l_0_config is missing else l_0_config), 'CURRENCY_SYMBOL'))
                yield '</span>'
                yield escape(t_1('%.0f', environment.getattr(l_1_p, 'discount_price')))
                yield '\n              </span>\n            '
            else:
                pass
                yield '\n              <span class="product-price"><span class="currency">'
                yield escape(environment.getattr((undefined(name='config') if l_0_config is missing else l_0_config), 'CURRENCY_SYMBOL'))
                yield '</span>'
                yield escape(t_1('%.0f', environment.getattr(l_1_p, 'price')))
                yield '</span>\n            '
            yield '\n            <button class="add-to-cart" onclick="event.stopPropagation(); addToCart('
            yield escape(environment.getattr(l_1_p, 'id'))
            yield ')"><i data-lucide="shopping-bag" style="width:11px;height:11px;margin-right:0.2rem;vertical-align:-1px;"></i>Add</button>\n          </div>\n        </div>\n      </div>\n      '
        l_1_loop = l_1_p = missing
        yield '\n    </div>\n  </div>\n  '
    yield '\n\n</section>\n'

blocks = {'title': block_title, 'content': block_content}
debug_info = '1=12&3=17&5=29&10=48&12=50&13=53&16=58&23=60&24=63&31=71&34=75&41=79&42=82&45=85&47=87&48=90&53=93&55=96&58=99&61=102&65=108&72=112&73=114&74=124&79=134&82=137&84=141&85=147&86=153&93=160&94=163&104=169&107=172&114=175&120=179&121=183&122=187&126=191&129=197&130=199&131=201&133=203&135=206&138=213&140=218'