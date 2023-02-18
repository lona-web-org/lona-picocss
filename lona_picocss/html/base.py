import json
import os

from lona.static_files import StyleSheet, Script, SORT_ORDER


def get_feather_icon_names():
    json_path = os.path.join(
        os.path.dirname(__file__),
        '../static/lona-picocss/dist/feather-icons/icons.json',
    )

    icons = json.loads(open(json_path, 'r').read())

    return list(icons.keys())


class PicocssNode:
    STATIC_FILES = [
        StyleSheet(
            name='pico.min.css',
            path='../static/lona-picocss/dist/pico/css/pico.min.css',
            url='/lona-picocss/dist/pico/css/pico.min.css',
            sort_order=SORT_ORDER.FRAMEWORK,
        ),
        StyleSheet(
            name='lona-picocss.css',
            path='../static/lona-picocss/lona-picocss.css',
            url='/lona-picocss/lona-picocss.css',
            sort_order=SORT_ORDER.LIBRARY,
        ),
        Script(
            name='picocss-widgets.js',
            path='../static/lona-picocss/picocss-widgets.js',
            url='/lona-picocss/picocss-widgets.js',
            sort_order=SORT_ORDER.LIBRARY,
        ),
    ]


class FeatherNode:
    STATIC_FILES = [
        Script(
            name='feather.min.js',
            path='../static/lona-picocss/dist/feather-icons/feather.min.js',
            url='/lona-picocss/dist/feather-icons/feather.min.js',
            sort_order=SORT_ORDER.FRAMEWORK,
        ),
        Script(
            name='feather-widgets.js',
            path='../static/lona-picocss/feather-widgets.js',
            url='/lona-picocss/feather-widgets.js',
            sort_order=SORT_ORDER.LIBRARY,
        ),
    ]
