from django.urls import include, path
from django.contrib import admin

from test_django_project.django_views import (
    forbidden_error_view,
    not_found_error_view,
    internal_error_view,
)

urlpatterns = [

    # admin
    path('django/admin/', admin.site.urls),

    # accounts
    path('django/accounts/', include('django.contrib.auth.urls')),

    # error pages
    path(
        'django/forbidden-error/',
        forbidden_error_view,
        name='forbidden-error',
    ),

    path(
        'django/not-found-error/',
        not_found_error_view,
        name='not-found-error',
    ),

    path(
        'django/internal-error/',
        internal_error_view,
        name='internal-error',
    ),
]

handler403 = 'lona_picocss.views.handler403'
handler404 = 'lona_picocss.views.handler404'
handler500 = 'lona_picocss.views.handler500'
