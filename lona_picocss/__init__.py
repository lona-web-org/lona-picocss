from lona import Route


from lona_picocss.views.components.typography import TypographyView
from lona_picocss.views.components.progress import ProgressView
from lona_picocss.views.components.buttons import ButtonsView
from lona_picocss.views.components.cards import CardsView
from lona_picocss.views.components.forms import FormsView
from lona_picocss.views.components.modal import ModalView
from lona_picocss.views.components.tabs import TabsView
from lona_picocss.views.settings import SettingsView
from lona_picocss.views.it_works import ItWorksView
from lona_picocss import settings

from lona_picocss.views.error_views import (
    InternalErrorView,
    Error404View,
    Error500View,
)


VERSION = (0, 1)
VERSION_STRING = '.'.join(str(i) for i in VERSION)


def install_picocss(app, debug=False):
    app.settings.PICOCSS_LONA_PROJECT_TYPE = 'app'

    # feature flags
    app.settings.CLIENT_VERSION = 2

    # setup settings
    app.settings.TEMPLATE_DIRS.append(settings.TEMPLATE_DIR)
    app.settings.STATIC_DIRS.append(settings.STATIC_DIR)
    app.settings.FRONTEND_TEMPLATE = settings.FRONTEND_TEMPLATE
    app.settings.FRONTEND_TEMPLATE = settings.FRONTEND_TEMPLATE
    app.settings.ERROR_404_VIEW = Error404View
    app.settings.ERROR_500_VIEW = Error500View

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

            # error views
            Route(
                '/_picocss/internal-error(/)',
                InternalErrorView,
                name='picocss__internal_error',
            ),
            Route(
                '/_picocss/settings(/)',
                SettingsView,
                name='picocss__settings',
            ),

            # component views
            Route(
                '/_picocss/components/typography(/)',
                TypographyView,
                name='picocss__components__typography',
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
        ])
