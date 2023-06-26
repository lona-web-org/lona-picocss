from lona.routing import MATCH_ALL, Route
from aiohttp_wsgi import WSGIHandler

from lona_picocss.routes import IT_WORKS_ROUTE, SETTINGS_ROUTE, DEMO_ROUTES
from lona_picocss.views.it_works import ItWorksView

from test_django_project._django.wsgi import application as django_application

django_wsgi_handler = WSGIHandler(django_application)

routes = [

    # lona-picocss
    Route('/', ItWorksView),
    IT_WORKS_ROUTE,
    SETTINGS_ROUTE,
    *DEMO_ROUTES,

    # django
    Route(MATCH_ALL, django_wsgi_handler, http_pass_through=True),
]
