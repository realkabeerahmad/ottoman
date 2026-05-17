from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'base.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_url_for = resolve('url_for')
    l_0_current_user = resolve('current_user')
    l_0_get_flashed_messages = resolve('get_flashed_messages')
    l_0_config = resolve('config')
    pass
    yield '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>'
    yield from context.blocks['title'][0](context)
    yield '</title>\n<link href="https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@400;700&family=Cinzel:wght@400;600;700&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&display=swap" rel="stylesheet">\n<link rel="stylesheet" href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'static', filename='css/style.css'))
    yield '">\n<script src="https://unpkg.com/lucide@latest"></script>\n'
    yield from context.blocks['styles'][0](context)
    yield '\n</head>\n<body>\n\n<!-- NAVIGATION -->\n<nav>\n  <a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'main.index'))
    yield '" class="nav-logo">\n    <i data-lucide="clock" style="width:18px;height:18px;stroke:var(--gold);margin-right:0.4rem;"></i>\n    Ottoman Time\n    <span>Timepieces of Empire</span>\n  </a>\n  <ul class="nav-links">\n    <li><a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'shop.collection'))
    yield '"><i data-lucide="layout-grid" style="width:13px;height:13px;margin-right:0.3rem;vertical-align:-1px;"></i>Collection</a></li>\n    <li><a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'main.index'))
    yield '#featured"><i data-lucide="star" style="width:13px;height:13px;margin-right:0.3rem;vertical-align:-1px;"></i>Signature</a></li>\n    <li><a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'main.index'))
    yield '#craft"><i data-lucide="gem" style="width:13px;height:13px;margin-right:0.3rem;vertical-align:-1px;"></i>Craft</a></li>\n    '
    if environment.getattr((undefined(name='current_user') if l_0_current_user is missing else l_0_current_user), 'is_authenticated'):
        pass
        yield '\n      '
        if context.call(environment.getattr((undefined(name='current_user') if l_0_current_user is missing else l_0_current_user), 'is_admin')):
            pass
            yield '\n        <li><a href="'
            yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.dashboard'))
            yield '" style="color: var(--gold);"><i data-lucide="shield" style="width:13px;height:13px;margin-right:0.3rem;vertical-align:-1px;"></i>Admin</a></li>\n      '
        yield '\n      <li><a href="'
        yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'auth.logout'))
        yield '"><i data-lucide="log-out" style="width:13px;height:13px;margin-right:0.3rem;vertical-align:-1px;"></i>Logout</a></li>\n    '
    else:
        pass
        yield '\n      <li><a href="'
        yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'auth.login'))
        yield '"><i data-lucide="user" style="width:13px;height:13px;margin-right:0.3rem;vertical-align:-1px;"></i>Account</a></li>\n    '
    yield '\n  </ul>\n  <div class="nav-actions">\n    <button class="cart-btn" onclick="toggleCart()">\n      <i data-lucide="shopping-bag" style="width:14px;height:14px;margin-right:0.3rem;vertical-align:-2px;"></i>\n      Cart\n      <span class="cart-count" id="cartCount">0</span>\n    </button>\n  </div>\n</nav>\n\n<!-- FLASH MESSAGES -->\n'
    l_1_messages = context.call((undefined(name='get_flashed_messages') if l_0_get_flashed_messages is missing else l_0_get_flashed_messages), with_categories=True)
    pass
    yield '\n  '
    if l_1_messages:
        pass
        yield '\n    <div style="position: fixed; top: 80px; right: 2rem; z-index: 9999; display: flex; flex-direction: column; gap: 0.5rem; max-width: 400px;">\n      '
        for (l_2_category, l_2_message) in l_1_messages:
            _loop_vars = {}
            pass
            yield '\n        <div class="flash-msg flash-'
            yield escape(l_2_category)
            yield '" style="\n          background: rgba(10,10,10,0.95);\n          border: 1px solid '
            if (l_2_category == 'error'):
                pass
                yield '#c0392b'
            elif (l_2_category == 'success'):
                pass
                yield 'var(--gold)'
            else:
                pass
                yield '#3498db'
            yield ';\n          color: '
            if (l_2_category == 'error'):
                pass
                yield '#e74c3c'
            elif (l_2_category == 'success'):
                pass
                yield 'var(--gold)'
            else:
                pass
                yield '#5dade2'
            yield ';\n          padding: 0.8rem 1.5rem;\n          font-family: \'Cinzel\', serif;\n          font-size: 0.8rem;\n          letter-spacing: 0.08em;\n          backdrop-filter: blur(10px);\n          animation: flashIn 0.3s ease, flashOut 0.3s ease 4s forwards;\n        ">\n          '
            yield escape(l_2_message)
            yield '\n        </div>\n      '
        l_2_category = l_2_message = missing
        yield '\n    </div>\n  '
    yield '\n'
    l_1_messages = missing
    yield '\n\n<!-- MAIN CONTENT -->\n<main>\n'
    yield from context.blocks['content'][0](context)
    yield '\n</main>\n\n<!-- FOOTER -->\n<footer>\n  <div class="footer-brand">\n    <span class="logo"><i data-lucide="clock" style="width:16px;height:16px;stroke:var(--gold);margin-right:0.4rem;vertical-align:-2px;"></i>Ottoman Time</span>\n    <span style="font-family:\'Cinzel\',serif;font-size:0.6rem;letter-spacing:0.3em;color:var(--gold-dark);text-transform:uppercase;">Timepieces of Empire</span>\n    <p>Crafted for those who understand that time is not merely measured — it is conquered.</p>\n  </div>\n  <div class="footer-col">\n    <h4><i data-lucide="watch" style="width:12px;height:12px;margin-right:0.4rem;vertical-align:-1px;"></i>Collection</h4>\n    <ul>\n      <li><a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'shop.collection'))
    yield '">All Timepieces</a></li>\n    </ul>\n  </div>\n  <div class="footer-col">\n    <h4><i data-lucide="hammer" style="width:12px;height:12px;margin-right:0.4rem;vertical-align:-1px;"></i>Atelier</h4>\n    <ul>\n      <li><a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'main.index'))
    yield '#craft">Our Craft</a></li>\n    </ul>\n  </div>\n  <div class="footer-col">\n    <h4><i data-lucide="mail" style="width:12px;height:12px;margin-right:0.4rem;vertical-align:-1px;"></i>House</h4>\n    <ul>\n      <li><a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'main.index'))
    yield '#contact">Contact</a></li>\n    </ul>\n  </div>\n</footer>\n<div class="footer-bottom">\n  <span>© 2025 Ottoman Time. All rights reserved.</span>\n  <span style="color:var(--gold);letter-spacing:0.3em;">◆ ◇ ◆</span>\n  <span><i data-lucide="map-pin" style="width:11px;height:11px;margin-right:0.3rem;vertical-align:-1px;"></i>Lahore · Istanbul · Geneva</span>\n</div>\n\n<!-- CART SIDEBAR -->\n<div class="cart-overlay" id="cartOverlay" onclick="toggleCart()"></div>\n<div class="cart-sidebar" id="cartSidebar">\n  <div class="cart-header">\n    <span class="cart-title">Your Acquisitions</span>\n    <button class="cart-close" onclick="toggleCart()">✕</button>\n  </div>\n  <div class="cart-items" id="cartItems">\n    <p class="cart-empty">Your collection awaits.<br><em>Add a timepiece to begin.</em></p>\n  </div>\n  <div class="cart-footer">\n    <div class="cart-total">\n      <span>Total</span>\n      <span id="cartTotal">'
    yield escape(environment.getattr((undefined(name='config') if l_0_config is missing else l_0_config), 'CURRENCY_SYMBOL'))
    yield '0</span>\n    </div>\n    <button class="checkout-btn" onclick="window.location.href=\''
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'shop.checkout'))
    yield '\'">Proceed to Acquire</button>\n  </div>\n</div>\n\n<!-- NOTIFICATION -->\n<div class="notification" id="notification"></div>\n\n<style>\n@keyframes flashIn {\n  from { opacity: 0; transform: translateX(30px); }\n  to { opacity: 1; transform: translateX(0); }\n}\n@keyframes flashOut {\n  from { opacity: 1; }\n  to { opacity: 0; transform: translateY(-10px); }\n}\n</style>\n\n<script>\nconst CURRENCY = \''
    yield escape(environment.getattr((undefined(name='config') if l_0_config is missing else l_0_config), 'CURRENCY_SYMBOL'))
    yield '\';\n\n// Cart toggle\nfunction toggleCart() {\n  document.getElementById(\'cartSidebar\').classList.toggle(\'open\');\n  document.getElementById(\'cartOverlay\').classList.toggle(\'open\');\n}\n\nfunction showNotification(msg) {\n  const n = document.getElementById(\'notification\');\n  n.textContent = msg;\n  n.classList.add(\'show\');\n  setTimeout(() => n.classList.remove(\'show\'), 3000);\n}\n\n// Load & render cart\nfunction loadCart() {\n  fetch(\'/shop/api/cart\')\n    .then(res => res.json())\n    .then(data => {\n      document.getElementById(\'cartCount\').textContent = data.total_items || 0;\n      document.getElementById(\'cartTotal\').textContent = CURRENCY + (data.subtotal || 0).toFixed(0);\n\n      const container = document.getElementById(\'cartItems\');\n      if (data.items && data.items.length > 0) {\n        container.innerHTML = data.items.map(item => `\n          <div class="cart-item" data-item-id="${item.id}">\n            <div class="cart-item-img">\n              ${item.image ? `<img src="${item.image}" style="width:100%;height:100%;object-fit:cover;">` : `<i data-lucide="watch" style="width:24px;height:24px;stroke:var(--gold);"></i>`}\n            </div>\n            <div class="cart-item-details">\n              <div class="cart-item-name">${item.name}</div>\n              <div class="cart-item-price">${CURRENCY}${item.price.toFixed(0)}${item.has_discount ? \' <small style="text-decoration:line-through;color:var(--text-dim);">\' + CURRENCY + item.original_price.toFixed(0) + \'</small>\' : \'\'}</div>\n              <div style="display:flex;align-items:center;gap:0.5rem;margin-top:0.4rem;">\n                <button onclick="updateQty(${item.id}, ${item.quantity - 1})" style="background:none;border:1px solid var(--glass-border);color:var(--gold);width:24px;height:24px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:background 0.3s;"><i data-lucide="minus" style="width:12px;height:12px;"></i></button>\n                <span style="font-family:\'Cinzel\',serif;font-size:0.8rem;color:var(--text-primary);min-width:20px;text-align:center;">${item.quantity}</span>\n                <button onclick="updateQty(${item.id}, ${item.quantity + 1})" style="background:none;border:1px solid var(--glass-border);color:var(--gold);width:24px;height:24px;cursor:pointer;display:flex;align-items:center;justify-content:center;transition:background 0.3s;"><i data-lucide="plus" style="width:12px;height:12px;"></i></button>\n              </div>\n            </div>\n            <div style="display:flex;flex-direction:column;align-items:flex-end;gap:0.5rem;">\n              <span style="color:var(--gold);font-family:\'Cinzel\',serif;font-size:0.9rem;">${CURRENCY}${item.line_total.toFixed(0)}</span>\n              <button class="cart-item-remove" onclick="removeItem(${item.id})" title="Remove"><i data-lucide="trash-2" style="width:14px;height:14px;"></i></button>\n            </div>\n          </div>\n        `).join(\'\');\n      } else {\n        container.innerHTML = \'<div style="text-align:center;padding:4rem 0;color:var(--text-dim);"><i data-lucide="shopping-bag" style="width:48px;height:48px;margin-bottom:1rem;opacity:0.5;"></i><p class="cart-empty" style="margin-top:0;">Your collection awaits.<br><em>Add a timepiece to begin.</em></p></div>\';\n      }\n      \n      // Re-initialize icons inside cart since DOM was replaced\n      if (typeof lucide !== \'undefined\') lucide.createIcons();\n    })\n    .catch(() => {});\n}\n\nfunction updateQty(itemId, newQty) {\n  fetch(`/shop/api/cart/update/${itemId}`, {\n    method: \'POST\',\n    headers: { \'Content-Type\': \'application/json\' },\n    body: JSON.stringify({ quantity: newQty })\n  })\n  .then(res => res.json())\n  .then(data => {\n    showNotification(data.message);\n    loadCart();\n  });\n}\n\nfunction removeItem(itemId) {\n  fetch(`/shop/api/cart/remove/${itemId}`, {\n    method: \'POST\',\n    headers: { \'Content-Type\': \'application/json\' }\n  })\n  .then(res => res.json())\n  .then(data => {\n    showNotification(data.message);\n    loadCart();\n  });\n}\n\nfunction addToCart(productId) {\n  fetch(`/shop/api/cart/add/${productId}`, {\n    method: \'POST\',\n    headers: { \'Content-Type\': \'application/json\' }\n  })\n  .then(res => res.json())\n  .then(data => {\n    showNotification(data.message || \'✦ Added to your collection\');\n    loadCart();\n  })\n  .catch(err => {\n    console.error(err);\n    showNotification(\'◆ Failed to add item\');\n  });\n}\n\nwindow.addEventListener(\'DOMContentLoaded\', () => {\n  loadCart();\n  \n  // Initialize Lucide icons\n  if (typeof lucide !== \'undefined\') lucide.createIcons();\n\n  // Scroll-reveal animation observer\n  const revealElements = document.querySelectorAll(\'.reveal\');\n  if (revealElements.length > 0) {\n    const revealObserver = new IntersectionObserver((entries) => {\n      entries.forEach((entry, index) => {\n        if (entry.isIntersecting) {\n          // Stagger the animation for sibling elements\n          const delay = entry.target.dataset.revealDelay || 0;\n          setTimeout(() => {\n            entry.target.classList.add(\'revealed\');\n          }, delay);\n          revealObserver.unobserve(entry.target);\n        }\n      });\n    }, { threshold: 0.1, rootMargin: \'0px 0px -40px 0px\' });\n\n    revealElements.forEach((el, i) => {\n      // Auto-stagger children if no explicit delay\n      if (!el.dataset.revealDelay) {\n        el.dataset.revealDelay = i * 80;\n      }\n      revealObserver.observe(el);\n    });\n  }\n});\n\nwindow.addEventListener(\'scroll\', () => {\n  const nav = document.querySelector(\'nav\');\n  nav.style.boxShadow = window.scrollY > 80 ? \'0 4px 40px rgba(0,0,0,0.6)\' : \'none\';\n});\n</script>\n'
    yield from context.blocks['scripts'][0](context)
    yield '\n</body>\n</html>'

def block_title(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    _block_vars = {}
    pass
    yield 'Ottoman Time — Timepieces of Empire'

def block_styles(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    _block_vars = {}
    pass

def block_content(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    _block_vars = {}
    pass

def block_scripts(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    _block_vars = {}
    pass

blocks = {'title': block_title, 'styles': block_styles, 'content': block_content, 'scripts': block_scripts}
debug_info = '6=16&8=18&10=20&16=22&22=24&23=26&24=28&25=30&26=33&27=36&29=39&31=44&45=50&47=53&48=57&50=59&51=69&59=79&68=86&81=88&87=90&93=92&116=94&118=96&137=98&270=100&6=103&10=113&68=122&270=131'