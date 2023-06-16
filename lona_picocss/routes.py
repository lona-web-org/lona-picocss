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

from lona_picocss.views.error_views import (
    ForbiddenErrorView,
    InternalErrorView,
)

from lona import Route

IT_WORKS_ROUTE = Route(
    '/_picocss/it-works(/)',
    ItWorksView,
    name='picocss__it_works',
)

SETTINGS_ROUTE = Route(
    '/_picocss/settings(/)',
    SettingsView,
    name='picocss__settings',
)

DEMO_ROUTES = [

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
]
