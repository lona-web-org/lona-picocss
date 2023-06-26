from lona_picocss import (
    get_django_auth_navigation,
    get_django_show_exceptions,
    get_debug_navigation,
    Error403View,
    Error404View,
    Error500View,
    settings,
    NavItem,
)

ROUTING_TABLE = 'routes.py::routes'

CLIENT_VERSION = 2

# middlewares
MIDDLEWARES = [
    'lona_picocss.middlewares.LonaPicocssMiddleware',
    'lona_picocss.middlewares.DjangoCollectStaticMiddleware',
    'lona_django.middlewares.DjangoSessionMiddleware',
]

# static files
STATIC_DIRS.extend([
    'static',
    settings.STATIC_DIR,
])

# templating
TEMPLATE_DIRS.append(settings.TEMPLATE_DIR)

FRONTEND_TEMPLATE = settings.FRONTEND_TEMPLATE
ERROR_403_VIEW = Error403View
ERROR_404_VIEW = Error404View
ERROR_500_VIEW = Error500View

PICOCSS_SHOW_EXCEPTIONS = get_django_show_exceptions


# navigation
def get_navigation(server, request):
    from django.shortcuts import reverse

    nav_items = []

    # lona-picocss debug navigation
    nav_items.extend(get_debug_navigation(server, request))

    # django debug views
    nav_items[-1].nav_items.extend([
        NavItem(
            title='Django Forbidden Error',
            url=reverse('forbidden-error'),
        ),
        NavItem(
            title='Django Not Found Error',
            url=reverse('not-found-error'),
        ),
        NavItem(
            title='Django Internal Error',
            url=reverse('internal-error'),
        ),
    ])

    # django auth navigation
    nav_items.extend(get_django_auth_navigation(server, request))

    return nav_items


PICOCSS_NAVIGATION = get_navigation
