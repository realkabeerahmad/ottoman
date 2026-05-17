from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'admin/admin_base.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_url_for = resolve('url_for')
    l_0_request = resolve('request')
    l_0_get_flashed_messages = resolve('get_flashed_messages')
    pass
    yield '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>'
    yield from context.blocks['title'][0](context)
    yield '</title>\n<link href="https://fonts.googleapis.com/css2?family=Cinzel+Decorative:wght@400;700&family=Cinzel:wght@400;600;700&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&display=swap" rel="stylesheet">\n<link rel="stylesheet" href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'static', filename='css/style.css'))
    yield '">\n<script src="https://unpkg.com/lucide@latest"></script>\n<style>\n  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }\n\n  .admin-layout {\n    display: flex;\n    min-height: 100vh;\n  }\n\n  /* ── SIDEBAR ── */\n  .admin-sidebar {\n    width: 260px;\n    background: linear-gradient(180deg, #0a0a0a 0%, #111 100%);\n    border-right: 1px solid rgba(201,168,76,0.12);\n    padding: 0;\n    display: flex;\n    flex-direction: column;\n    position: fixed;\n    height: 100vh;\n    overflow-y: auto;\n    z-index: 100;\n  }\n  .admin-sidebar::-webkit-scrollbar { width: 4px; }\n  .admin-sidebar::-webkit-scrollbar-thumb { background: rgba(201,168,76,0.2); border-radius: 2px; }\n\n  .sidebar-brand {\n    text-align: center;\n    padding: 2rem 1.5rem 1.5rem;\n    border-bottom: 1px solid rgba(201,168,76,0.1);\n  }\n  .sidebar-brand a {\n    text-decoration: none;\n    display: block;\n  }\n  .sidebar-brand .brand-name {\n    font-family: \'Cinzel Decorative\', serif;\n    color: var(--gold);\n    font-size: 1.1rem;\n    display: block;\n    margin-bottom: 0.3rem;\n  }\n  .sidebar-brand .brand-sub {\n    font-family: \'Cinzel\', serif;\n    font-size: 0.55rem;\n    letter-spacing: 0.3em;\n    color: rgba(201,168,76,0.4);\n    text-transform: uppercase;\n  }\n\n  .sidebar-section {\n    padding: 1.2rem 0 0.5rem;\n  }\n  .sidebar-section-title {\n    padding: 0 1.5rem;\n    font-family: \'Cinzel\', serif;\n    font-size: 0.6rem;\n    letter-spacing: 0.25em;\n    text-transform: uppercase;\n    color: rgba(201,168,76,0.35);\n    margin-bottom: 0.5rem;\n  }\n  .sidebar-nav {\n    list-style: none;\n  }\n  .sidebar-nav a {\n    display: flex;\n    align-items: center;\n    gap: 0.8rem;\n    padding: 0.75rem 1.5rem;\n    color: rgba(255,255,255,0.5);\n    text-decoration: none;\n    font-family: \'Cinzel\', serif;\n    font-size: 0.72rem;\n    letter-spacing: 0.1em;\n    text-transform: uppercase;\n    transition: all 0.25s ease;\n    border-left: 3px solid transparent;\n  }\n  .sidebar-nav a:hover {\n    background: rgba(201,168,76,0.06);\n    color: var(--gold);\n    border-left-color: rgba(201,168,76,0.3);\n  }\n  .sidebar-nav a.active {\n    background: rgba(201,168,76,0.08);\n    color: var(--gold);\n    border-left-color: var(--gold);\n  }\n  .sidebar-nav .nav-icon {\n    font-size: 1rem;\n    width: 1.2rem;\n    text-align: center;\n  }\n\n  .sidebar-footer {\n    margin-top: auto;\n    padding: 1rem 0;\n    border-top: 1px solid rgba(201,168,76,0.1);\n  }\n  .sidebar-footer a {\n    color: rgba(255,255,255,0.3) !important;\n  }\n  .sidebar-footer a.logout-link {\n    color: rgba(192,57,43,0.6) !important;\n  }\n  .sidebar-footer a.logout-link:hover {\n    color: #c0392b !important;\n    background: rgba(192,57,43,0.08);\n  }\n\n  /* ── MAIN CONTENT ── */\n  .admin-main {\n    flex: 1;\n    margin-left: 260px;\n    padding: 2rem 3rem;\n    min-height: 100vh;\n    background: #0d0d0d;\n  }\n\n  /* ── FLASH MESSAGES ── */\n  .admin-flash {\n    padding: 0.8rem 1.5rem;\n    margin-bottom: 1.5rem;\n    font-family: \'Cinzel\', serif;\n    font-size: 0.8rem;\n    letter-spacing: 0.08em;\n    border-left: 3px solid;\n    background: rgba(0,0,0,0.3);\n  }\n  .admin-flash.success {\n    border-color: var(--gold);\n    color: var(--gold);\n  }\n  .admin-flash.error {\n    border-color: #c0392b;\n    color: #e74c3c;\n  }\n  .admin-flash.info {\n    border-color: #3498db;\n    color: #5dade2;\n  }\n\n  /* ── PAGE HEADER ── */\n  .page-header {\n    display: flex;\n    justify-content: space-between;\n    align-items: center;\n    margin-bottom: 2rem;\n    padding-bottom: 1.5rem;\n    border-bottom: 1px solid rgba(201,168,76,0.1);\n  }\n  .page-title {\n    font-family: \'Cinzel Decorative\', serif;\n    color: var(--gold);\n    font-size: 1.6rem;\n  }\n  .page-subtitle {\n    font-family: \'Cinzel\', serif;\n    font-size: 0.7rem;\n    color: rgba(255,255,255,0.3);\n    letter-spacing: 0.15em;\n    text-transform: uppercase;\n    margin-top: 0.3rem;\n  }\n\n  /* ── STAT CARDS ── */\n  .stats-grid {\n    display: grid;\n    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));\n    gap: 1.5rem;\n    margin-bottom: 2.5rem;\n  }\n  .stat-card {\n    background: rgba(255,255,255,0.02);\n    border: 1px solid rgba(201,168,76,0.1);\n    padding: 1.5rem;\n    transition: border-color 0.3s;\n  }\n  .stat-card:hover {\n    border-color: rgba(201,168,76,0.25);\n  }\n  .stat-label {\n    font-family: \'Cinzel\', serif;\n    font-size: 0.65rem;\n    color: rgba(255,255,255,0.35);\n    text-transform: uppercase;\n    letter-spacing: 0.2em;\n    margin-bottom: 0.8rem;\n  }\n  .stat-value {\n    font-size: 2rem;\n    font-family: \'Cinzel Decorative\', serif;\n    color: var(--gold);\n  }\n\n  /* ── DATA TABLE ── */\n  .data-table {\n    width: 100%;\n    border-collapse: collapse;\n    background: rgba(255,255,255,0.02);\n    border: 1px solid rgba(201,168,76,0.1);\n  }\n  .data-table th {\n    padding: 1rem 1.2rem;\n    font-family: \'Cinzel\', serif;\n    font-size: 0.7rem;\n    color: rgba(255,255,255,0.35);\n    text-transform: uppercase;\n    letter-spacing: 0.12em;\n    text-align: left;\n    border-bottom: 1px solid rgba(201,168,76,0.1);\n    background: rgba(0,0,0,0.2);\n  }\n  .data-table td {\n    padding: 0.9rem 1.2rem;\n    border-bottom: 1px solid rgba(255,255,255,0.04);\n    font-family: \'Cormorant Garamond\', serif;\n    font-size: 1rem;\n    color: rgba(255,255,255,0.7);\n  }\n  .data-table tr:hover td {\n    background: rgba(201,168,76,0.03);\n  }\n  .data-table .empty-row td {\n    text-align: center;\n    padding: 3rem;\n    color: rgba(255,255,255,0.2);\n    font-style: italic;\n  }\n  .data-table .gold { color: var(--gold); }\n  .data-table .muted { color: rgba(255,255,255,0.35); }\n  .data-table .mono { font-family: monospace; font-size: 0.85rem; }\n\n  /* ── ACTION LINKS ── */\n  .action-link {\n    text-decoration: none;\n    font-family: \'Cinzel\', serif;\n    font-size: 0.75rem;\n    letter-spacing: 0.05em;\n    margin-right: 1rem;\n    transition: opacity 0.2s;\n  }\n  .action-link:hover { opacity: 0.8; }\n  .action-link.manage { color: rgba(255,255,255,0.5); }\n  .action-link.edit { color: var(--gold); }\n  .action-link.delete { color: #c0392b; }\n  .action-link.view { color: var(--gold); }\n\n  /* ── FORMS ── */\n  .admin-form-card {\n    background: rgba(255,255,255,0.02);\n    border: 1px solid rgba(201,168,76,0.1);\n    padding: 2.5rem;\n    max-width: 700px;\n  }\n  .admin-form-title {\n    font-family: \'Cinzel Decorative\', serif;\n    font-size: 1.4rem;\n    color: var(--gold);\n    margin-bottom: 2rem;\n  }\n  .form-group {\n    margin-bottom: 1.5rem;\n  }\n  .form-label {\n    display: block;\n    font-family: \'Cinzel\', serif;\n    font-size: 0.65rem;\n    color: rgba(255,255,255,0.35);\n    letter-spacing: 0.2em;\n    text-transform: uppercase;\n    margin-bottom: 0.5rem;\n  }\n  .form-input {\n    width: 100%;\n    background: transparent;\n    border: none;\n    border-bottom: 1px solid rgba(201,168,76,0.15);\n    color: rgba(255,255,255,0.85);\n    padding: 0.6rem 0;\n    font-family: \'Cormorant Garamond\', serif;\n    font-size: 1.1rem;\n    outline: none;\n    transition: border-color 0.3s;\n  }\n  .form-input:focus {\n    border-bottom-color: var(--gold);\n  }\n  .form-select {\n    width: 100%;\n    background: #111;\n    border: 1px solid rgba(201,168,76,0.15);\n    color: rgba(255,255,255,0.85);\n    padding: 0.6rem;\n    font-family: \'Cormorant Garamond\', serif;\n    font-size: 1.05rem;\n    outline: none;\n    margin-top: 0.3rem;\n    transition: border-color 0.3s;\n  }\n  .form-select:focus {\n    border-color: var(--gold);\n  }\n  .form-row {\n    display: flex;\n    gap: 1.5rem;\n  }\n  .form-row > * { flex: 1; }\n  .form-actions {\n    display: flex;\n    gap: 1rem;\n    margin-top: 2rem;\n  }\n  .form-actions > * { flex: 1; text-align: center; }\n\n  .form-checkbox {\n    display: flex;\n    align-items: center;\n    gap: 0.6rem;\n    font-family: \'Cinzel\', serif;\n    font-size: 0.75rem;\n    color: rgba(255,255,255,0.5);\n    letter-spacing: 0.1em;\n    text-transform: uppercase;\n    cursor: pointer;\n  }\n\n  /* ── BUTTONS ── */\n  .btn-admin-primary {\n    display: inline-block;\n    padding: 0.7rem 1.8rem;\n    background: linear-gradient(135deg, #C9A84C, #8B6914);\n    color: #0a0a0a;\n    font-family: \'Cinzel\', serif;\n    font-size: 0.75rem;\n    letter-spacing: 0.15em;\n    text-transform: uppercase;\n    text-decoration: none;\n    border: none;\n    cursor: pointer;\n    transition: all 0.3s;\n  }\n  .btn-admin-primary:hover {\n    background: linear-gradient(135deg, #E8CC85, #C9A84C);\n  }\n  .btn-admin-secondary {\n    display: inline-block;\n    padding: 0.7rem 1.8rem;\n    background: transparent;\n    color: rgba(255,255,255,0.5);\n    font-family: \'Cinzel\', serif;\n    font-size: 0.75rem;\n    letter-spacing: 0.15em;\n    text-transform: uppercase;\n    text-decoration: none;\n    border: 1px solid rgba(255,255,255,0.15);\n    cursor: pointer;\n    transition: all 0.3s;\n  }\n  .btn-admin-secondary:hover {\n    border-color: rgba(255,255,255,0.3);\n    color: rgba(255,255,255,0.8);\n  }\n\n  /* ── BADGE ── */\n  .badge {\n    display: inline-block;\n    padding: 0.2rem 0.6rem;\n    font-family: \'Cinzel\', serif;\n    font-size: 0.6rem;\n    letter-spacing: 0.1em;\n    text-transform: uppercase;\n    border-radius: 2px;\n  }\n  .badge-active { background: rgba(39,174,96,0.15); color: #27ae60; }\n  .badge-inactive { background: rgba(192,57,43,0.15); color: #c0392b; }\n  .badge-warning { background: rgba(243,156,18,0.15); color: #f39c12; }\n\n  /* Delete form inline */\n  .delete-form {\n    display: inline;\n  }\n  .delete-form button {\n    background: none;\n    border: none;\n    cursor: pointer;\n    font-family: \'Cinzel\', serif;\n    font-size: 0.75rem;\n    letter-spacing: 0.05em;\n    color: #c0392b;\n    transition: opacity 0.2s;\n  }\n  .delete-form button:hover { opacity: 0.7; }\n</style>\n'
    yield from context.blocks['styles'][0](context)
    yield '\n</head>\n<body>\n\n<div class="admin-layout">\n  <aside class="admin-sidebar">\n    <div class="sidebar-brand">\n      <a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.dashboard'))
    yield '">\n        <span class="brand-name">Inner Court</span>\n        <span class="brand-sub">Administration</span>\n      </a>\n    </div>\n\n    <div class="sidebar-section">\n      <div class="sidebar-section-title">Overview</div>\n      <ul class="sidebar-nav">\n        <li><a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.dashboard'))
    yield '" class="'
    if (environment.getattr((undefined(name='request') if l_0_request is missing else l_0_request), 'endpoint') == 'admin.dashboard'):
        pass
        yield 'active'
    yield '">\n          <span class="nav-icon"><i data-lucide="layout-dashboard" style="width:16px;height:16px;"></i></span> Dashboard\n        </a></li>\n      </ul>\n    </div>\n\n    <div class="sidebar-section">\n      <div class="sidebar-section-title">Catalog</div>\n      <ul class="sidebar-nav">\n        <li><a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.manage_products'))
    yield '" class="'
    if ('product' in (environment.getattr((undefined(name='request') if l_0_request is missing else l_0_request), 'endpoint') or '')):
        pass
        yield 'active'
    yield '">\n          <span class="nav-icon"><i data-lucide="watch" style="width:16px;height:16px;"></i></span> Products\n        </a></li>\n        <li><a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.manage_categories'))
    yield '" class="'
    if ('categor' in (environment.getattr((undefined(name='request') if l_0_request is missing else l_0_request), 'endpoint') or '')):
        pass
        yield 'active'
    yield '">\n          <span class="nav-icon"><i data-lucide="folder-tree" style="width:16px;height:16px;"></i></span> Categories\n        </a></li>\n      </ul>\n    </div>\n\n    <div class="sidebar-section">\n      <div class="sidebar-section-title">Sales</div>\n      <ul class="sidebar-nav">\n        <li><a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.manage_orders'))
    yield '" class="'
    if (('order' in (environment.getattr((undefined(name='request') if l_0_request is missing else l_0_request), 'endpoint') or '')) and ('status' not in (environment.getattr((undefined(name='request') if l_0_request is missing else l_0_request), 'endpoint') or ''))):
        pass
        yield 'active'
    yield '">\n          <span class="nav-icon"><i data-lucide="receipt" style="width:16px;height:16px;"></i></span> Orders\n        </a></li>\n        <li><a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.manage_coupons'))
    yield '" class="'
    if ('coupon' in (environment.getattr((undefined(name='request') if l_0_request is missing else l_0_request), 'endpoint') or '')):
        pass
        yield 'active'
    yield '">\n          <span class="nav-icon"><i data-lucide="ticket" style="width:16px;height:16px;"></i></span> Discounts\n        </a></li>\n      </ul>\n    </div>\n\n    <div class="sidebar-section">\n      <div class="sidebar-section-title">Configuration</div>\n      <ul class="sidebar-nav">\n        <li><a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.manage_shipping'))
    yield '" class="'
    if ('shipping' in (environment.getattr((undefined(name='request') if l_0_request is missing else l_0_request), 'endpoint') or '')):
        pass
        yield 'active'
    yield '">\n          <span class="nav-icon"><i data-lucide="package" style="width:16px;height:16px;"></i></span> Shipping\n        </a></li>\n        <li><a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.manage_payment_methods'))
    yield '" class="'
    if ('payment' in (environment.getattr((undefined(name='request') if l_0_request is missing else l_0_request), 'endpoint') or '')):
        pass
        yield 'active'
    yield '">\n          <span class="nav-icon"><i data-lucide="credit-card" style="width:16px;height:16px;"></i></span> Payments\n        </a></li>\n        <li><a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'admin.manage_order_statuses'))
    yield '" class="'
    if ('status' in (environment.getattr((undefined(name='request') if l_0_request is missing else l_0_request), 'endpoint') or '')):
        pass
        yield 'active'
    yield '">\n          <span class="nav-icon"><i data-lucide="tags" style="width:16px;height:16px;"></i></span> Order Statuses\n        </a></li>\n      </ul>\n    </div>\n\n    <div class="sidebar-footer">\n      <ul class="sidebar-nav">\n        <li><a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'main.index'))
    yield '">\n          <span class="nav-icon"><i data-lucide="arrow-left" style="width:16px;height:16px;"></i></span> Return to Store\n        </a></li>\n        <li><a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'auth.logout'))
    yield '" class="logout-link">\n          <span class="nav-icon"><i data-lucide="log-out" style="width:16px;height:16px;"></i></span> Logout\n        </a></li>\n      </ul>\n    </div>\n  </aside>\n\n  <main class="admin-main">\n    '
    l_1_messages = context.call((undefined(name='get_flashed_messages') if l_0_get_flashed_messages is missing else l_0_get_flashed_messages), with_categories=True)
    pass
    yield '\n      '
    if l_1_messages:
        pass
        yield '\n        '
        for (l_2_category, l_2_message) in l_1_messages:
            _loop_vars = {}
            pass
            yield '\n          <div class="admin-flash '
            yield escape(l_2_category)
            yield '">'
            yield escape(l_2_message)
            yield '</div>\n        '
        l_2_category = l_2_message = missing
        yield '\n      '
    yield '\n    '
    l_1_messages = missing
    yield '\n\n    '
    yield from context.blocks['content'][0](context)
    yield "\n  </main>\n</div>\n\n<script>\n  document.addEventListener('DOMContentLoaded', () => {\n    if (typeof lucide !== 'undefined') {\n      lucide.createIcons();\n    }\n  });\n</script>\n</body>\n</html>"

def block_title(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    _block_vars = {}
    pass
    yield 'Inner Court — Admin'

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

blocks = {'title': block_title, 'styles': block_styles, 'content': block_content}
debug_info = '6=15&8=17&403=19&410=21&419=23&428=29&431=35&440=41&443=47&452=53&455=59&458=65&466=71&469=73&478=78&479=81&480=85&485=94&6=97&403=107&485=116'