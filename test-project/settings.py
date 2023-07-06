from lona_picocss.middlewares import LonaPicocssMiddleware
from lona_picocss import settings, get_debug_navigation

from lona_picocss.views.error_views import (
    Error403View,
    Error404View,
    Error500View,
)

ROUTING_TABLE = 'routes.py::routes'

CLIENT_VERSION = 2

# middlewares
MIDDLEWARES = [
    LonaPicocssMiddleware,
]

# static files
STATIC_DIRS.append(settings.STATIC_DIR)

# templating
TEMPLATE_DIRS.append(settings.TEMPLATE_DIR)

FRONTEND_TEMPLATE = settings.FRONTEND_TEMPLATE
ERROR_403_VIEW = Error403View
ERROR_404_VIEW = Error404View
ERROR_500_VIEW = Error500View

PICOCSS_NAVIGATION = get_debug_navigation
