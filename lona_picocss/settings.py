import os

from lona_picocss.color_schemes import COLOR_SCHEMES

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static')
FRONTEND_TEMPLATE = 'picocss/base.html'

SETTINGS_DEFAULTS = {
    'PICOCSS_DEBUG': False,
    'PICOCSS_BRAND': 'Lona',
    'PICOCSS_LOGO': 'lona-picocss/logo.svg',
    'PICOCSS_TITLE': 'Lona',
    'PICOCSS_AUTO_RECONNECT': True,
    'PICOCSS_SHOW_EXCEPTIONS': True,
    'PICOCSS_THEME': ['dark', 'light'],  # FIXME: add 'auto'
    'PICOCSS_COLOR_SCHEME': list(COLOR_SCHEMES.keys()),
    'PICOCSS_PAGE_WIDTH': '',
    'PICOCSS_HEADER': True,
    'PICOCSS_FOOTER': True,
    'PICOCSS_FLUID': False,
    'PICOCSS_NAVIGATION': [],
}

CSS_VARIABLES_DEFAULTS = {
    'PICOCSS_FONT_FAMILY': 'system-ui, -apple-system, "Segoe UI", "Roboto", "Ubuntu", "Cantarell", "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',  # NOQA
    'PICOCSS_FONT_SIZE': '16px',
    'PICOCSS_FONT_WEIGHT': '400',
    'PICOCSS_LINE_HEIGHT': '1.5',
    'PICOCSS_BORDER_RADIUS': '0.25rem',
    'PICOCSS_BORDER_WIDTH': '1px',
    'PICOCSS_OUTLINE_WIDTH': '3px',
    'PICOCSS_SPACING': '1rem',
    'PICOCSS_TYPOGRAPHY_SPACING_VERTICAL': '1.5rem',
    'PICOCSS_BLOCK_SPACING_VERTICAL': 'calc(var(--spacing) * 2)',
    'PICOCSS_BLOCK_SPACING_HORIZONTAL': 'var(--spacing)',
    'PICOCSS_GRID_SPACING_VERTICAL': '0',
    'PICOCSS_GRID_SPACING_HORIZONTAL': 'var(--spacing)',
    'PICOCSS_FORM_ELEMENT_SPACING_VERTICAL': '0.75rem',
    'PICOCSS_FORM_ELEMENT_SPACING_HORIZONTAL': '1rem',
    'PICOCSS_NAV_ELEMENT_SPACING_VERTICAL': '1rem',
    'PICOCSS_NAV_ELEMENT_SPACING_HORIZONTAL': '0.5rem',
    'PICOCSS_NAV_LINK_SPACING_VERTICAL': '0.5rem',
    'PICOCSS_NAV_LINK_SPACING_HORIZONTAL': '0.5rem',
    'PICOCSS_FORM_LABEL_FONT_WEIGHT': 'var(--font-weight)',
}

_lona_server = None
_settings = {}
_css_variables = {}
_css_string = ''


def set_lona_server(lona_server):
    global _lona_server

    _lona_server = lona_server


# settings ####################################################################
def get_names():
    return [
        *SETTINGS_DEFAULTS.keys(),
        *CSS_VARIABLES_DEFAULTS.keys(),
    ]


def get(name):
    if name in _settings:
        return _settings[name]

    elif name in _css_variables:
        return _css_variables[name]

    raise KeyError(f'unknown setting name: {name}')


def set(name, value):
    if name in SETTINGS_DEFAULTS:
        _settings[name] = value

    elif name in CSS_VARIABLES_DEFAULTS:
        _css_variables[name] = value

    else:
        raise KeyError(f'unknown setting name: {name}')


def get_default(name, fallback=''):
    if name in SETTINGS_DEFAULTS:
        return SETTINGS_DEFAULTS[name]

    elif name in CSS_VARIABLES_DEFAULTS:
        return CSS_VARIABLES_DEFAULTS[name]

    return fallback


def reset():
    _settings.clear()
    _css_variables.clear()

    # settings
    for key, value in SETTINGS_DEFAULTS.items():
        if isinstance(value, list) and len(value) > 0:
            value = value[0]

        _settings[key] = value

    # css variables
    for key, value in CSS_VARIABLES_DEFAULTS.items():
        if isinstance(value, list) and len(value) > 0:
            value = value[0]

        _css_variables[key] = value


def load_lona_settings():
    names = get_names()

    # pull settings from lona settings
    for name in _lona_server.settings:
        if name not in names:
            continue

        set(name, _lona_server.settings.get(name))


def render_theme():
    global _css_string

    _css_string = _lona_server.render_template(
        template_name='picocss/color-scheme.css',
        template_context={
            'hex_to_rgba': hex_to_rgba,
            'theme_data': get_theme_data(),
        },
    )


# templating ##################################################################
def get_theme_data(request=None):

    # logo
    logo_path = get('PICOCSS_LOGO')

    if logo_path:
        logo_path = os.path.join(
            _lona_server.settings.STATIC_URL_PREFIX,
            logo_path,
        )

    # navigation
    if request is None:
        navigation = []

    else:
        navigation = get('PICOCSS_NAVIGATION')

        if callable(navigation):
            navigation = navigation(_lona_server, request)

    # show_exceptions
    show_exceptions = get('PICOCSS_SHOW_EXCEPTIONS')

    if callable(show_exceptions):
        if request is None:
            show_exceptions = False

        else:
            show_exceptions = show_exceptions(_lona_server, request)

    # theme data
    theme_data = {
        'color_scheme': COLOR_SCHEMES[get('PICOCSS_COLOR_SCHEME')],
        'theme_settings': {},
        'css_variables': {},
        'css_string': _css_string,
        'logo_path': logo_path,
        'navigation': navigation,
        'show_exceptions': show_exceptions,

        'stylesheet_urls': [
            os.path.join(
                _lona_server.settings.STATIC_URL_PREFIX,
                'lona-picocss/dist/pico/css/pico.min.css',
            ),
            os.path.join(
                _lona_server.settings.STATIC_URL_PREFIX,
                'lona-picocss/lona-picocss.css',
            ),
        ],

        'script_urls': [
            os.path.join(
                _lona_server.settings.STATIC_URL_PREFIX,
                'lona-picocss/dist/feather-icons/feather.min.js',
            ),
        ],
    }

    for key, value in _settings.items():
        name = key[len('PICOCSS_'):].lower()
        theme_data['theme_settings'][name] = value

    for key, value in _css_variables.items():
        name = key[len('PICOCSS_'):].lower().replace('_', '-')
        theme_data['css_variables'][name] = value

    return theme_data


def hex_to_rgba(hex, alpha):
    if hex.startswith('#'):
        hex = hex[1:]

    if len(hex) == 3:
        hex = f'{hex[0]*2}{hex[1]*2}{hex[2]*2}'

    red, green, blue = [int(hex[i:i+2], 16) for i in (0, 2, 4)]

    return f'rgba({red}, {green}, {blue}, {alpha})'
