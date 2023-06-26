from django.utils.safestring import mark_safe
from django import template

from lona_picocss.settings import get_theme_data as _get_theme_data
from lona_picocss.utils import exception_to_html as _exception_to_html

register = template.Library()


@register.simple_tag(takes_context=True)
def get_theme_data(context):
    context['theme_data'] = _get_theme_data(
        request=context['request'],
    )

    return ''


@register.filter
def exception_to_html(exception):
    return mark_safe(
        _exception_to_html(exception),
    )
