from lona_picocss.routes import IT_WORKS_ROUTE, SETTINGS_ROUTE, DEMO_ROUTES
from lona_picocss.middlewares import LonaPicocssMiddleware
from lona_picocss.utils import get_django_show_exceptions  # NOQA
from lona_picocss import settings

from lona_picocss.navigation import (  # NOQA
    get_django_auth_navigation,
    get_debug_navigation,
    NavItem,
    NavDivider,
)

from lona_picocss.views.error_views import (
    Error403View,
    Error404View,
    Error500View,
)


VERSION = (0, 4, 3)
VERSION_STRING = '.'.join(str(i) for i in VERSION)


def install_picocss(app, debug=False):
    app.settings.PICOCSS_LONA_PROJECT_TYPE = 'app'
    app.settings.PICOCSS_DEBUG = debug

    # feature flags
    app.settings.CLIENT_VERSION = 2

    # setup settings
    app.settings.TEMPLATE_DIRS.append(settings.TEMPLATE_DIR)
    app.settings.STATIC_DIRS.append(settings.STATIC_DIR)
    app.settings.FRONTEND_TEMPLATE = settings.FRONTEND_TEMPLATE
    app.settings.ERROR_403_VIEW = Error403View
    app.settings.ERROR_404_VIEW = Error404View
    app.settings.ERROR_500_VIEW = Error500View

    # setup middlewares
    app.middleware(LonaPicocssMiddleware)

    # setup views
    app.routes.append(IT_WORKS_ROUTE)

    if debug:
        app.routes.extend([
            SETTINGS_ROUTE,
            *DEMO_ROUTES,
        ])

        if 'PICOCSS_NAVIGATION' not in app.settings:
            app.settings.PICOCSS_NAVIGATION = get_debug_navigation
