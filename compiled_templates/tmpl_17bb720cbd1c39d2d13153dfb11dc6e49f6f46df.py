from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'shop/collection.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('base.html', 'shop/collection.html')
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
    l_0_categories = resolve('categories')
    l_0_featured_categories = resolve('featured_categories')
    l_0_products = resolve('products')
    try:
        t_1 = environment.filters['format']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'format' found.")
    try:
        t_2 = environment.filters['list']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'list' found.")
    try:
        t_3 = environment.filters['selectattr']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'selectattr' found.")
    pass
    yield '\n<section id="collection" style="padding-top: 120px;">\n  <div class="collection">\n    <div class="section-header reveal">\n      <span class="section-label"><i data-lucide="watch" style="width:14px;height:14px;margin-right:0.3rem;vertical-align:-2px;"></i> The Collection <i data-lucide="watch" style="width:14px;height:14px;margin-left:0.3rem;vertical-align:-2px;"></i></span>\n      <h2 class="section-title">Timepieces of Conquest</h2>\n      <p class="section-desc">Each watch carries the soul of an empire — forged in precision, adorned in legacy.</p>\n    </div>\n\n    <!-- CATEGORY FILTER BAR -->\n    <div class="collection-filter reveal" data-reveal-delay="200">\n      <button class="filter-btn active" onclick="filterProducts(\'all\', this)"><i data-lucide="grid-3x3" style="width:11px;height:11px;margin-right:0.3rem;vertical-align:-1px;"></i>All</button>\n      '
    for l_1_category in (undefined(name='categories') if l_0_categories is missing else l_0_categories):
        _loop_vars = {}
        pass
        yield '\n        '
        if (not environment.getattr(l_1_category, 'parent_id')):
            pass
            yield '\n        <button class="filter-btn '
            if environment.getattr(l_1_category, 'is_featured'):
                pass
                yield 'featured-filter'
            yield '" onclick="filterProducts(\''
            yield escape(environment.getattr(l_1_category, 'slug'))
            yield '\', this)">\n          '
            if environment.getattr(l_1_category, 'is_featured'):
                pass
                yield '<i data-lucide="star" style="width:10px;height:10px;margin-right:0.2rem;vertical-align:-1px;"></i>'
            yield escape(environment.getattr(l_1_category, 'name'))
            yield '\n        </button>\n        '
            for l_2_child in environment.getattr(l_1_category, 'subcategories'):
                _loop_vars = {}
                pass
                yield '\n          '
                if (environment.getattr(l_2_child, 'status') == 'active'):
                    pass
                    yield '\n          <button class="filter-btn" onclick="filterProducts(\''
                    yield escape(environment.getattr(l_2_child, 'slug'))
                    yield '\', this)" style="font-size: 0.55rem; padding: 0.35rem 1rem; border-left: 2px solid var(--gold-dark);">\n            <i data-lucide="corner-down-right" style="width:9px;height:9px;margin-right:0.2rem;vertical-align:-1px;"></i>'
                    yield escape(environment.getattr(l_2_child, 'name'))
                    yield '\n          </button>\n          '
                yield '\n        '
            l_2_child = missing
            yield '\n        '
        yield '\n      '
    l_1_category = missing
    yield '\n    </div>\n\n    <!-- FEATURED CATEGORY SECTIONS -->\n    '
    l_1_loop = missing
    for l_1_cat, l_1_loop in LoopContext((undefined(name='featured_categories') if l_0_featured_categories is missing else l_0_featured_categories), undefined):
        l_1_cat_products = missing
        _loop_vars = {}
        pass
        yield '\n    '
        l_1_cat_products = t_2(context.eval_ctx, t_3(context, t_3(context, (undefined(name='products') if l_0_products is missing else l_0_products), 'category'), 'category.id', 'equalto', environment.getattr(l_1_cat, 'id')))
        _loop_vars['cat_products'] = l_1_cat_products
        yield '\n    '
        if (undefined(name='cat_products') if l_1_cat_products is missing else l_1_cat_products):
            pass
            yield '\n    <div class="featured-category-section reveal" data-category-slug="'
            yield escape(environment.getattr(l_1_cat, 'slug'))
            yield '">\n      <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 2rem;">\n        <div style="height: 1px; flex: 1; background: linear-gradient(to right, transparent, var(--glass-border));"></div>\n        <h3 style="font-family: \'Cinzel Decorative\', serif; color: var(--gold); font-size: 1.3rem; white-space: nowrap;">\n          <i data-lucide="sparkles" style="width:16px;height:16px;margin-right:0.4rem;vertical-align:-2px;"></i>'
            yield escape(environment.getattr(l_1_cat, 'name'))
            yield ' Collection\n        </h3>\n        <div style="height: 1px; flex: 1; background: linear-gradient(to left, transparent, var(--glass-border));"></div>\n      </div>\n      '
            if environment.getattr(l_1_cat, 'description'):
                pass
                yield '\n      <p style="text-align: center; color: var(--text-muted); font-style: italic; margin-bottom: 2rem; max-width: 600px; margin-left: auto; margin-right: auto;">'
                yield escape(environment.getattr(l_1_cat, 'description'))
                yield '</p>\n      '
            yield '\n      <div class="products-grid" style="margin-bottom: 4rem;">\n        '
            l_2_loop = missing
            for l_2_product, l_2_loop in LoopContext((undefined(name='cat_products') if l_1_cat_products is missing else l_1_cat_products), undefined):
                l_2_url_for = resolve('url_for')
                l_2_config = resolve('config')
                _loop_vars = {}
                pass
                yield '\n        <div class="product-card reveal" data-category="'
                yield escape((environment.getattr(environment.getattr(l_2_product, 'category'), 'slug') if environment.getattr(l_2_product, 'category') else 'uncategorized'))
                yield '" data-reveal-delay="'
                yield escape((environment.getattr(l_2_loop, 'index0') * 100))
                yield '" onclick="window.location.href=\''
                yield escape(context.call((undefined(name='url_for') if l_2_url_for is missing else l_2_url_for), 'shop.product_detail', slug=environment.getattr(l_2_product, 'slug'), _loop_vars=_loop_vars))
                yield '\'">\n          '
                if environment.getattr(l_2_product, 'is_featured'):
                    pass
                    yield '\n          <span class="product-badge"><i data-lucide="award" style="width:10px;height:10px;margin-right:0.2rem;vertical-align:-1px;"></i>Featured</span>\n          '
                yield '\n          <div class="product-img">\n            <div class="watch-illustration" style="'
                if environment.getattr(l_2_product, 'main_image'):
                    pass
                    yield "background-image: url('"
                    yield escape(environment.getattr(l_2_product, 'main_image'))
                    yield "'); background-size: cover;"
                yield '"></div>\n          </div>\n          <div class="product-info">\n            <span class="product-collection-tag">'
                yield escape((environment.getattr(environment.getattr(l_2_product, 'category'), 'name') if environment.getattr(l_2_product, 'category') else 'Ottoman Time'))
                yield '</span>\n            <h3 class="product-name"><a href="'
                yield escape(context.call((undefined(name='url_for') if l_2_url_for is missing else l_2_url_for), 'shop.product_detail', slug=environment.getattr(l_2_product, 'slug'), _loop_vars=_loop_vars))
                yield '" style="color: inherit; text-decoration: none;">'
                yield escape(environment.getattr(l_2_product, 'name'))
                yield '</a></h3>\n            <p class="product-desc">'
                yield escape((environment.getattr(l_2_product, 'short_description') or ''))
                yield '</p>\n            <div class="product-footer">\n              '
                if environment.getattr(l_2_product, 'discount_price'):
                    pass
                    yield '\n                <span class="product-price">\n                  <span class="currency">'
                    yield escape(environment.getattr((undefined(name='config') if l_2_config is missing else l_2_config), 'CURRENCY_SYMBOL'))
                    yield '</span>'
                    yield escape(t_1('%.0f', environment.getattr(l_2_product, 'discount_price')))
                    yield '\n                  <small style="text-decoration: line-through; color: var(--text-dim); margin-left: 0.5rem;">'
                    yield escape(environment.getattr((undefined(name='config') if l_2_config is missing else l_2_config), 'CURRENCY_SYMBOL'))
                    yield escape(t_1('%.0f', environment.getattr(l_2_product, 'price')))
                    yield '</small>\n                </span>\n              '
                else:
                    pass
                    yield '\n                <span class="product-price"><span class="currency">'
                    yield escape(environment.getattr((undefined(name='config') if l_2_config is missing else l_2_config), 'CURRENCY_SYMBOL'))
                    yield '</span>'
                    yield escape(t_1('%.0f', environment.getattr(l_2_product, 'price')))
                    yield '</span>\n              '
                yield '\n              <button class="add-to-cart" onclick="event.stopPropagation(); addToCart('
                yield escape(environment.getattr(l_2_product, 'id'))
                yield ')"><i data-lucide="shopping-bag" style="width:11px;height:11px;margin-right:0.2rem;vertical-align:-1px;"></i>Add</button>\n            </div>\n          </div>\n        </div>\n        '
            l_2_loop = l_2_product = l_2_url_for = l_2_config = missing
            yield '\n      </div>\n    </div>\n    '
        yield '\n    '
    l_1_loop = l_1_cat = l_1_cat_products = missing
    yield '\n\n    <!-- ALL PRODUCTS GRID -->\n    <div id="allProductsSection">\n      <div class="reveal" style="display: flex; align-items: center; gap: 1rem; margin-bottom: 2rem;">\n        <div style="height: 1px; flex: 1; background: linear-gradient(to right, transparent, var(--glass-border));"></div>\n        <h3 style="font-family: \'Cinzel Decorative\', serif; color: var(--text-muted); font-size: 1.1rem; white-space: nowrap;">\n          <i data-lucide="layout-grid" style="width:14px;height:14px;margin-right:0.4rem;vertical-align:-2px;"></i>All Timepieces\n        </h3>\n        <div style="height: 1px; flex: 1; background: linear-gradient(to left, transparent, var(--glass-border));"></div>\n      </div>\n\n      <div class="products-grid" id="productsGrid">\n        '
    l_1_loop = missing
    t_4 = 1
    for l_1_product, l_1_loop in LoopContext((undefined(name='products') if l_0_products is missing else l_0_products), undefined):
        l_1_url_for = resolve('url_for')
        l_1_config = resolve('config')
        _loop_vars = {}
        pass
        yield '\n        <div class="product-card reveal" data-category="'
        yield escape((environment.getattr(environment.getattr(l_1_product, 'category'), 'slug') if environment.getattr(l_1_product, 'category') else 'uncategorized'))
        yield '" data-reveal-delay="'
        yield escape((environment.getattr(l_1_loop, 'index0') * 80))
        yield '" onclick="window.location.href=\''
        yield escape(context.call((undefined(name='url_for') if l_1_url_for is missing else l_1_url_for), 'shop.product_detail', slug=environment.getattr(l_1_product, 'slug'), _loop_vars=_loop_vars))
        yield '\'">\n          '
        if environment.getattr(l_1_product, 'is_featured'):
            pass
            yield '\n          <span class="product-badge"><i data-lucide="award" style="width:10px;height:10px;margin-right:0.2rem;vertical-align:-1px;"></i>Featured</span>\n          '
        yield '\n          <div class="product-img">\n            <div class="watch-illustration" style="'
        if environment.getattr(l_1_product, 'main_image'):
            pass
            yield "background-image: url('"
            yield escape(environment.getattr(l_1_product, 'main_image'))
            yield "'); background-size: cover;"
        yield '"></div>\n          </div>\n          <div class="product-info">\n            <span class="product-collection-tag">'
        yield escape((environment.getattr(environment.getattr(l_1_product, 'category'), 'name') if environment.getattr(l_1_product, 'category') else 'Ottoman Time'))
        yield '</span>\n            <h3 class="product-name"><a href="'
        yield escape(context.call((undefined(name='url_for') if l_1_url_for is missing else l_1_url_for), 'shop.product_detail', slug=environment.getattr(l_1_product, 'slug'), _loop_vars=_loop_vars))
        yield '" style="color: inherit; text-decoration: none;">'
        yield escape(environment.getattr(l_1_product, 'name'))
        yield '</a></h3>\n            <p class="product-desc">'
        yield escape((environment.getattr(l_1_product, 'short_description') or ''))
        yield '</p>\n            <div class="product-footer">\n              '
        if environment.getattr(l_1_product, 'discount_price'):
            pass
            yield '\n                <span class="product-price">\n                  <span class="currency">'
            yield escape(environment.getattr((undefined(name='config') if l_1_config is missing else l_1_config), 'CURRENCY_SYMBOL'))
            yield '</span>'
            yield escape(t_1('%.0f', environment.getattr(l_1_product, 'discount_price')))
            yield '\n                  <small style="text-decoration: line-through; color: var(--text-dim); margin-left: 0.5rem;">'
            yield escape(environment.getattr((undefined(name='config') if l_1_config is missing else l_1_config), 'CURRENCY_SYMBOL'))
            yield escape(t_1('%.0f', environment.getattr(l_1_product, 'price')))
            yield '</small>\n                </span>\n              '
        else:
            pass
            yield '\n                <span class="product-price"><span class="currency">'
            yield escape(environment.getattr((undefined(name='config') if l_1_config is missing else l_1_config), 'CURRENCY_SYMBOL'))
            yield '</span>'
            yield escape(t_1('%.0f', environment.getattr(l_1_product, 'price')))
            yield '</span>\n              '
        yield '\n              <button class="add-to-cart" onclick="event.stopPropagation(); addToCart('
        yield escape(environment.getattr(l_1_product, 'id'))
        yield ')"><i data-lucide="shopping-bag" style="width:11px;height:11px;margin-right:0.2rem;vertical-align:-1px;"></i>Add</button>\n            </div>\n          </div>\n        </div>\n        '
        t_4 = 0
    l_1_loop = l_1_product = l_1_url_for = l_1_config = missing
    if t_4:
        pass
        yield '\n          <p style="text-align:center; color: var(--text-dim); grid-column: 1/-1; padding: 3rem 0;">No timepieces found in our current catalog.</p>\n        '
    yield '\n      </div>\n    </div>\n  </div>\n</section>\n'

def block_scripts(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    _block_vars = {}
    l_0_category_tree = resolve('category_tree')
    try:
        t_5 = environment.filters['tojson']
    except KeyError:
        @internalcode
        def t_5(*unused):
            raise TemplateRuntimeError("No filter named 'tojson' found.")
    pass
    yield '\n<script>\n// Category hierarchy: parent-slug -> [child slugs]\nconst CATEGORY_TREE = '
    yield escape(t_5(context.eval_ctx, (undefined(name='category_tree') if l_0_category_tree is missing else l_0_category_tree)))
    yield ";\n\nfunction getSlugsForFilter(slug) {\n  if (CATEGORY_TREE[slug]) {\n    return [slug, ...CATEGORY_TREE[slug]];\n  }\n  return [slug];\n}\n\nfunction filterProducts(cat, btn) {\n  document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));\n  btn.classList.add('active');\n\n  const featuredSections = document.querySelectorAll('.featured-category-section');\n  const allSection = document.getElementById('allProductsSection');\n  const allCards = document.querySelectorAll('#productsGrid .product-card');\n\n  if (cat === 'all') {\n    featuredSections.forEach(s => s.style.display = 'block');\n    allSection.style.display = 'block';\n    allCards.forEach(card => card.style.display = 'flex');\n  } else {\n    const matchingSlugs = getSlugsForFilter(cat);\n\n    featuredSections.forEach(s => {\n      s.style.display = matchingSlugs.includes(s.dataset.categorySlug) ? 'block' : 'none';\n    });\n\n    allSection.style.display = 'block';\n    allCards.forEach(card => {\n      card.style.display = matchingSlugs.includes(card.dataset.category) ? 'flex' : 'none';\n    });\n  }\n}\n</script>\n"

blocks = {'content': block_content, 'scripts': block_scripts}
debug_info = '1=12&3=17&15=47&16=51&17=54&18=60&20=65&21=69&22=72&23=74&32=83&33=88&34=91&35=94&39=96&43=98&44=101&47=105&48=111&49=117&53=121&56=127&57=129&58=133&60=135&62=138&63=142&66=148&68=153&89=162&90=168&91=174&95=178&98=184&99=186&100=190&102=192&104=195&105=199&108=205&110=210&123=219&126=235'