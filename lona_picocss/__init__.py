import logging

from lona import Route

from lona_picocss.views.components.typography import TypographyView
from lona_picocss.views.components.scroller import ScrollerView
from lona_picocss.views.components.progress import ProgressView
from lona_picocss.views.components.buttons import ButtonsView
from lona_picocss.views.components.cards import CardsView
from lona_picocss.views.components.icons import IconsView
from lona_picocss.views.components.forms import FormsView
from lona_picocss.views.components.modal import ModalView
from lona_picocss.views.components.tabs import TabsView
from lona_picocss.views.settings import SettingsView
from lona_picocss.views.it_works import ItWorksView
from lona_picocss import settings

from lona_picocss.views.error_views import (
    ForbiddenErrorView,
    InternalErrorView,
    Error403View,
    Error404View,
    Error500View,
)


VERSION = (0, 3)
VERSION_STRING = '.'.join(str(i) for i in VERSION)

logger = logging.getLogger('lona-picocss')


def install_picocss(app, debug=False):
    app.settings.PICOCSS_LONA_PROJECT_TYPE = 'app'

    # feature flags
    app.settings.CLIENT_VERSION = 2

    # setup settings
    app.settings.TEMPLATE_DIRS.append(settings.TEMPLATE_DIR)
    app.settings.STATIC_DIRS.append(settings.STATIC_DIR)
    app.settings.FRONTEND_TEMPLATE = settings.FRONTEND_TEMPLATE
    app.settings.FRONTEND_TEMPLATE = settings.FRONTEND_TEMPLATE
    app.settings.ERROR_403_VIEW = Error403View
    app.settings.ERROR_404_VIEW = Error404View
    app.settings.ERROR_500_VIEW = Error500View

    # setup middlewares
    @app.middleware
    class PicocssDebugWarningMiddleware:
        async def on_startup(self, data):
            # this has do be done using a middleware, so the warning gets
            # logged after the logging is fully setup (color, format, etc)

            logger.warning('running in debug mode')

    # setup views
    app.routes.append(
        Route(
            '/_picocss/it-works(/)',
            ItWorksView,
            name='picocss__it_works',
        ),
    )

    if debug:
        app.routes.extend([

            # settings
            Route(
                '/_picocss/settings(/)',
                SettingsView,
                name='picocss__settings',
            ),

            # error views
            Route(
                '/_picocss/internal-error(/)',
                InternalErrorView,
                name='picocss__internal_error',
            ),
            Route(
                '/_picocss/forbidden-error(/)',
                ForbiddenErrorView,
                name='picocss__forbidden_error',
            ),

            # component views
            Route(
                '/_picocss/components/typography(/)',
                TypographyView,
                name='picocss__components__typography',
            ),
            Route(
                '/_picocss/components/icons(/)',
                IconsView,
                name='picocss__components__icons',
            ),
            Route(
                '/_picocss/components/cards(/)',
                CardsView,
                name='picocss__components__cards',
            ),
            Route(
                '/_picocss/components/forms(/)',
                FormsView,
                name='picocss__components__forms',
            ),
            Route(
                '/_picocss/components/buttons(/)',
                ButtonsView,
                name='picocss__components__buttons',
            ),
            Route(
                '/_picocss/components/progress(/)',
                ProgressView,
                name='picocss__components__progress',
            ),
            Route(
                '/_picocss/components/tabs(/)',
                TabsView,
                name='picocss__components__tabs',
            ),
            Route(
                '/_picocss/components/modal(/)',
                ModalView,
                name='picocss__components__modal',
            ),
            Route(
                '/_picocss/components/scroller(/)',
                ScrollerView,
                name='picocss__components__scroller',
            ),
        ])

        if 'PICOCSS_MENU' not in app.settings:
            app.settings.PICOCSS_MENU = settings.DEFAULT_MENU
