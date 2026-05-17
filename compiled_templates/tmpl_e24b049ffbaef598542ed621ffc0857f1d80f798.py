from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'main/index.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('base.html', 'main/index.html')
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
    yield '\n<!-- HERO -->\n<section class="hero">\n  <div class="hero-bg"></div>\n\n  <!-- Ottoman geometric mandala SVG — slow spin animation -->\n  <svg class="hero-mandala" style="animation: spin 120s linear infinite;" viewBox="0 0 700 700" xmlns="http://www.w3.org/2000/svg" fill="none" stroke="#C9A84C" stroke-width="0.8">\n    <circle cx="350" cy="350" r="340"/>\n    <circle cx="350" cy="350" r="280"/>\n    <circle cx="350" cy="350" r="220"/>\n    <circle cx="350" cy="350" r="160"/>\n    <circle cx="350" cy="350" r="100"/>\n    <polygon points="350,10 664,535 36,535" />\n    <polygon points="350,690 36,165 664,165" />\n    <polygon points="10,350 535,36 535,664" />\n    <polygon points="690,350 165,664 165,36" />\n    <line x1="350" y1="10" x2="350" y2="690"/>\n    <line x1="10" y1="350" x2="690" y2="350"/>\n    <line x1="105" y1="105" x2="595" y2="595"/>\n    <line x1="595" y1="105" x2="105" y2="595"/>\n    <circle cx="350" cy="350" r="40"/>\n    <circle cx="350" cy="350" r="20"/>\n    <g transform="rotate(22.5,350,350)">\n      <polygon points="350,10 664,535 36,535" />\n      <polygon points="350,690 36,165 664,165" />\n    </g>\n  </svg>\n\n  <div class="hero-content">\n    <p class="hero-eyebrow" style="animation: fadeInDown 1s 0.3s both;">Est. The Golden Age</p>\n    <h1 style="animation: fadeInDown 1s 0.6s both;">Ottoman<em>Time</em></h1>\n    <p class="hero-subtitle" style="animation: fadeInDown 1s 0.9s both;">Where the grandeur of empire meets the precision of horology. Each timepiece is a conquest of craft.</p>\n    <div class="hero-cta" style="animation: fadeInDown 1s 1.2s both;">\n      <a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'shop.collection', _block_vars=_block_vars))
    yield '" class="btn-primary"><i data-lucide="compass" style="width:14px;height:14px;margin-right:0.4rem;vertical-align:-2px;"></i>Explore Collection</a>\n      <a href="#featured" class="btn-secondary"><i data-lucide="star" style="width:14px;height:14px;margin-right:0.4rem;vertical-align:-2px;"></i>Our Signature</a>\n    </div>\n  </div>\n\n  <div class="hero-scroll" style="animation: fadeInDown 1s 1.5s both;">\n    <div class="scroll-line"></div>\n    <span><i data-lucide="chevron-down" style="width:12px;height:12px;margin-right:0.3rem;vertical-align:-1px;"></i>Scroll</span>\n  </div>\n</section>\n\n<!-- HERITAGE -->\n<div class="heritage">\n  <div class="heritage-grid">\n    <div class="heritage-item reveal" data-reveal-delay="0">\n      <span class="heritage-num"><i data-lucide="crown" style="width:20px;height:20px;margin-right:0.4rem;vertical-align:-3px;stroke:var(--gold);"></i>600+</span>\n      <span class="heritage-label">Years of Empire Heritage</span>\n    </div>\n    <div class="heritage-item reveal" data-reveal-delay="100">\n      <span class="heritage-num"><i data-lucide="gem" style="width:20px;height:20px;margin-right:0.4rem;vertical-align:-3px;stroke:var(--gold);"></i>18K</span>\n      <span class="heritage-label">Gold Alloy Cases</span>\n    </div>\n    <div class="heritage-item reveal" data-reveal-delay="200">\n      <span class="heritage-num"><i data-lucide="battery-charging" style="width:20px;height:20px;margin-right:0.4rem;vertical-align:-3px;stroke:var(--gold);"></i>72h</span>\n      <span class="heritage-label">Power Reserve</span>\n    </div>\n    <div class="heritage-item reveal" data-reveal-delay="300">\n      <span class="heritage-num"><i data-lucide="infinity" style="width:20px;height:20px;margin-right:0.4rem;vertical-align:-3px;stroke:var(--gold);"></i>∞</span>\n      <span class="heritage-label">Lifetime Craftsmanship</span>\n    </div>\n  </div>\n</div>\n\n<!-- FEATURED PRODUCTS -->\n<section id="featured" class="collection" style="padding: 6rem 4rem;">\n  <div class="section-header reveal">\n    <span class="section-label"><i data-lucide="sparkles" style="width:14px;height:14px;margin-right:0.3rem;vertical-align:-2px;"></i> Signature Pieces <i data-lucide="sparkles" style="width:14px;height:14px;margin-left:0.3rem;vertical-align:-2px;"></i></span>\n    <h2 class="section-title">Featured Timepieces</h2>\n    <p class="section-desc">Our most distinguished creations, hand-selected for the discerning collector.</p>\n  </div>\n\n  '
    if (undefined(name='products') if l_0_products is missing else l_0_products):
        pass
        yield '\n  <div class="products-grid" style="max-width: 1400px; margin: 0 auto;">\n    '
        l_1_loop = missing
        for l_1_product, l_1_loop in LoopContext((undefined(name='products') if l_0_products is missing else l_0_products), undefined):
            l_1_config = resolve('config')
            _loop_vars = {}
            pass
            yield '\n    <div class="product-card reveal" data-reveal-delay="'
            yield escape((environment.getattr(l_1_loop, 'index0') * 120))
            yield '" onclick="window.location.href=\''
            yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'shop.product_detail', slug=environment.getattr(l_1_product, 'slug'), _loop_vars=_loop_vars))
            yield '\'">\n      <span class="product-badge"><i data-lucide="award" style="width:10px;height:10px;margin-right:0.3rem;vertical-align:-1px;"></i>Signature</span>\n      <div class="product-img">\n        <div class="watch-illustration" style="'
            if environment.getattr(l_1_product, 'main_image'):
                pass
                yield "background-image: url('"
                yield escape(environment.getattr(l_1_product, 'main_image'))
                yield "'); background-size: cover;"
            yield '"></div>\n      </div>\n      <div class="product-info">\n        <span class="product-collection-tag">'
            yield escape((environment.getattr(environment.getattr(l_1_product, 'category'), 'name') if environment.getattr(l_1_product, 'category') else 'Ottoman Time'))
            yield '</span>\n        <h3 class="product-name"><a href="'
            yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'shop.product_detail', slug=environment.getattr(l_1_product, 'slug'), _loop_vars=_loop_vars))
            yield '" style="color: inherit; text-decoration: none;">'
            yield escape(environment.getattr(l_1_product, 'name'))
            yield '</a></h3>\n        <p class="product-desc">'
            yield escape((environment.getattr(l_1_product, 'short_description') or ''))
            yield '</p>\n        <div class="product-footer">\n          '
            if environment.getattr(l_1_product, 'discount_price'):
                pass
                yield '\n            <span class="product-price">\n              <span class="currency">'
                yield escape(environment.getattr((undefined(name='config') if l_1_config is missing else l_1_config), 'CURRENCY_SYMBOL'))
                yield '</span>'
                yield escape(t_1('%.0f', environment.getattr(l_1_product, 'discount_price')))
                yield '\n              <small style="text-decoration: line-through; color: var(--text-dim); margin-left: 0.5rem;">'
                yield escape(environment.getattr((undefined(name='config') if l_1_config is missing else l_1_config), 'CURRENCY_SYMBOL'))
                yield escape(t_1('%.0f', environment.getattr(l_1_product, 'price')))
                yield '</small>\n            </span>\n          '
            else:
                pass
                yield '\n            <span class="product-price"><span class="currency">'
                yield escape(environment.getattr((undefined(name='config') if l_1_config is missing else l_1_config), 'CURRENCY_SYMBOL'))
                yield '</span>'
                yield escape(t_1('%.0f', environment.getattr(l_1_product, 'price')))
                yield '</span>\n          '
            yield '\n          <button class="add-to-cart" onclick="event.stopPropagation(); addToCart('
            yield escape(environment.getattr(l_1_product, 'id'))
            yield ')"><i data-lucide="shopping-bag" style="width:11px;height:11px;margin-right:0.3rem;vertical-align:-1px;"></i>Add</button>\n        </div>\n      </div>\n    </div>\n    '
        l_1_loop = l_1_product = l_1_config = missing
        yield '\n  </div>\n  <div class="reveal" data-reveal-delay="400" style="text-align: center; margin-top: 3rem;">\n    <a href="'
        yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'shop.collection', _block_vars=_block_vars))
        yield '" class="btn-secondary"><i data-lucide="arrow-right" style="width:14px;height:14px;margin-right:0.4rem;vertical-align:-2px;"></i>View Full Collection</a>\n  </div>\n  '
    else:
        pass
        yield '\n  <p style="text-align: center; color: var(--text-dim); font-style: italic; font-size: 1.1rem;">Featured pieces coming soon. Mark products as featured in the admin dashboard.</p>\n  '
    yield '\n</section>\n\n<!-- CRAFT -->\n<section id="craft" class="craft">\n  <div class="section-header reveal">\n    <span class="section-label"><i data-lucide="hexagon" style="width:14px;height:14px;margin-right:0.3rem;vertical-align:-2px;"></i> Our Philosophy <i data-lucide="hexagon" style="width:14px;height:14px;margin-left:0.3rem;vertical-align:-2px;"></i></span>\n    <h2 class="section-title">The Art of Imperial Craft</h2>\n  </div>\n  <div class="craft-grid">\n    <div class="craft-item reveal" data-reveal-delay="0">\n      <div style="margin-bottom: 1.5rem;">\n        <i data-lucide="landmark" style="width:48px;height:48px;stroke:var(--gold);stroke-width:1;"></i>\n      </div>\n      <h3 class="craft-title">Ottoman Heritage</h3>\n      <p class="craft-text">Every design draws from six centuries of Ottoman artistry — geometric tessellations, arabesque patterns, and celestial motifs that once adorned the halls of Topkapı Palace.</p>\n    </div>\n    <div class="craft-item reveal" data-reveal-delay="150">\n      <div style="margin-bottom: 1.5rem;">\n        <i data-lucide="settings" style="width:48px;height:48px;stroke:var(--gold);stroke-width:1;"></i>\n      </div>\n      <h3 class="craft-title">Mechanical Precision</h3>\n      <p class="craft-text">Each movement is assembled by master watchmakers in our atelier, with hundreds of hand-finished components achieving tolerances measured in microns.</p>\n    </div>\n    <div class="craft-item reveal" data-reveal-delay="300">\n      <div style="margin-bottom: 1.5rem;">\n        <i data-lucide="diamond" style="width:48px;height:48px;stroke:var(--gold);stroke-width:1;"></i>\n      </div>\n      <h3 class="craft-title">18K Gold Mastery</h3>\n      <p class="craft-text">Our cases are cast, machined, and finished entirely in-house from 18-karat gold alloys — each surface polished to a mirror or satin finish by hand over eight painstaking hours.</p>\n    </div>\n  </div>\n</section>\n\n<!-- NEWSLETTER -->\n<section class="newsletter reveal" id="contact">\n  <div class="ornate-divider">◆ ◇ ◆</div>\n  <h2><i data-lucide="mail" style="width:24px;height:24px;margin-right:0.6rem;vertical-align:-4px;"></i>Enter the Inner Court</h2>\n  <p>Receive exclusive access to new collections, private viewings, and the stories behind each timepiece.</p>\n  <div class="newsletter-form">\n    <input type="email" placeholder="Your email address..." id="emailInput"/>\n    <button onclick="subscribeNewsletter()"><i data-lucide="send" style="width:13px;height:13px;margin-right:0.4rem;vertical-align:-1px;"></i>Subscribe</button>\n  </div>\n</section>\n\n'

def block_scripts(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    _block_vars = {}
    pass
    yield "\n<style>\n@keyframes fadeInDown {\n  from { opacity: 0; transform: translateY(-20px); }\n  to { opacity: 1; transform: translateY(0); }\n}\n</style>\n<script>\nfunction subscribeNewsletter() {\n  const email = document.getElementById('emailInput').value;\n  if (!email.includes('@')) { showNotification('◆ Please enter a valid email'); return; }\n  showNotification('✦ Welcome to the inner court, distinguished guest');\n  document.getElementById('emailInput').value = '';\n}\n</script>\n"

blocks = {'content': block_content, 'scripts': block_scripts}
debug_info = '1=12&3=17&36=34&77=36&79=40&80=45&83=49&86=55&87=57&88=61&90=63&92=66&93=70&96=76&98=81&105=85&156=92'