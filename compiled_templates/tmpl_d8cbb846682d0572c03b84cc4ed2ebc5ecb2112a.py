from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'auth/login.html'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    parent_template = None
    pass
    parent_template = environment.get_template('base.html', 'auth/login.html')
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
    l_0_get_flashed_messages = resolve('get_flashed_messages')
    l_0_url_for = resolve('url_for')
    pass
    yield '\n<section class="auth-section" style="padding: 120px 4rem 8rem; min-height: 80vh; display: flex; align-items: center; justify-content: center;">\n  <div class="auth-box" style="background: var(--glass); border: 1px solid var(--glass-border); padding: 4rem; max-width: 500px; width: 100%; text-align: center;">\n    <h2 style="font-family: \'Cinzel Decorative\', serif; font-size: 2rem; color: var(--gold); margin-bottom: 2rem;">Enter the Court</h2>\n    \n    '
    l_1_messages = context.call((undefined(name='get_flashed_messages') if l_0_get_flashed_messages is missing else l_0_get_flashed_messages), with_categories=True, _block_vars=_block_vars)
    pass
    yield '\n      '
    if l_1_messages:
        pass
        yield '\n        '
        for (l_2_category, l_2_message) in l_1_messages:
            _loop_vars = {}
            pass
            yield '\n          <div style="color: '
            if (l_2_category == 'error'):
                pass
                yield '#c0392b'
            else:
                pass
                yield 'var(--gold)'
            yield '; font-family: \'Cinzel\', serif; font-size: 0.8rem; margin-bottom: 1.5rem; letter-spacing: 0.1em; border: 1px solid; padding: 0.5rem;">\n            '
            yield escape(l_2_message)
            yield '\n          </div>\n        '
        l_2_category = l_2_message = missing
        yield '\n      '
    yield '\n    '
    l_1_messages = missing
    yield '\n\n    <form method="POST" action="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'auth.login', _block_vars=_block_vars))
    yield '" style="display: flex; flex-direction: column; gap: 1.5rem; text-align: left;">\n      <div>\n        <label for="email" style="font-family: \'Cinzel\', serif; font-size: 0.7rem; color: var(--text-muted); letter-spacing: 0.2em; text-transform: uppercase;">Email Address</label>\n        <input type="email" id="email" name="email" required style="width: 100%; background: transparent; border: none; border-bottom: 1px solid var(--glass-border); color: var(--text-primary); padding: 0.5rem 0; font-family: \'Cormorant Garamond\', serif; font-size: 1.1rem; outline: none; transition: border-color 0.3s;" onfocus="this.style.borderColor=\'var(--gold)\'" onblur="this.style.borderColor=\'var(--glass-border)\'">\n      </div>\n      <div>\n        <label for="password" style="font-family: \'Cinzel\', serif; font-size: 0.7rem; color: var(--text-muted); letter-spacing: 0.2em; text-transform: uppercase;">Password</label>\n        <input type="password" id="password" name="password" required style="width: 100%; background: transparent; border: none; border-bottom: 1px solid var(--glass-border); color: var(--text-primary); padding: 0.5rem 0; font-family: \'Cormorant Garamond\', serif; font-size: 1.1rem; outline: none; transition: border-color 0.3s;" onfocus="this.style.borderColor=\'var(--gold)\'" onblur="this.style.borderColor=\'var(--glass-border)\'">\n      </div>\n      \n      <button type="submit" class="btn-primary" style="margin-top: 1rem; width: 100%;">Authenticate</button>\n    </form>\n    \n    <div style="margin-top: 2rem; font-style: italic; color: var(--text-dim);">\n      Not a member of the court? <a href="'
    yield escape(context.call((undefined(name='url_for') if l_0_url_for is missing else l_0_url_for), 'auth.register', _block_vars=_block_vars))
    yield '" style="color: var(--gold); text-decoration: none;">Request Access</a>\n    </div>\n  </div>\n</section>\n'

blocks = {'content': block_content}
debug_info = '1=12&3=17&9=31&10=34&11=38&12=45&18=52&32=54'