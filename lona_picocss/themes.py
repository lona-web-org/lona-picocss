from lona_picocss import settings


def hex_to_rgba(hex, alpha):
    if hex.startswith('#'):
        hex = hex[1:]

    if len(hex) == 3:
        hex = f'{hex[0]*2}{hex[1]*2}{hex[2]*2}'

    red, green, blue = [int(hex[i:i+2], 16) for i in (0, 2, 4)]

    return f'rgba({red}, {green}, {blue}, {alpha})'


def get_theme_data(lona):
    theme_data = {
        'theme_settings': {},
        'css_variables': {},
        'color_scheme': {},
        'menu': lona.server.settings.get('PICOCSS_MENU', []) or [],
    }

    # theme settings
    for key in settings.THEME_SETTINGS.keys():
        name = key[len('PICOCSS_'):].lower()
        value = lona.settings.get(key, settings.DEFAULTS[key])
        theme_data['theme_settings'][name] = value

    # css variables
    for key in settings.CSS_VARIABLES.keys():
        name = key[len('PICOCSS_'):].lower()
        value = lona.settings.get(key, settings.DEFAULTS[key])
        theme_data['css_variables'][name.replace('_', '-')] = value

    # color scheme
    color_scheme_name = lona.settings.get(
        'PICOCSS_COLOR_SCHEME',
        settings.DEFAULTS['PICOCSS_COLOR_SCHEME'],
    )

    theme_data['color_scheme'] = settings.COLOR_SCHEMES[color_scheme_name]

    return theme_data


def resolve_url(lona, url):
    if url.startswith('!'):
        url = lona.server.reverse(route_name=url[1:])

    return url
