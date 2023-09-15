import os
from django import template
from django.conf import settings
from django.templatetags.static import static
from django.utils.html import mark_safe
import urllib.parse

register = template.Library()


@register.simple_tag()
def vue_bundle_url(bundle: str) -> str:
    """
    Return the url to a vue bundle. 'bundle' should match the input name as defined in vite.config.js.
    """
    extension = '.ts' if settings.VUE_FRONTEND_USE_TYPESCRIPT and settings.VUE_FRONTEND_USE_DEV_SERVER else '.js'
    if settings.VUE_FRONTEND_USE_DEV_SERVER:
        return urllib.parse.urljoin(
            settings.VUE_FRONTEND_DEV_SERVER_URL,
            settings.VUE_FRONTEND_DEV_SERVER_PATH + bundle + extension
        )
    else:
        return static(os.path.join(settings.VUE_FRONTEND_STATIC_DIR, bundle + extension))


@register.simple_tag()
def vue_provide(key: str, value: str) -> str:
    """
    Specify a key value pair which will be 'provided' to the Vue application. It can later be injected in most places,
    such as components or Pinia stores, with `inject('key_name')`
    """
    return mark_safe(
        {% raw %}f'<script>window.vueProvided = window.vueProvided || {{}}; vueProvided["{key}"] = "{value}";</script>'{% endraw %}
    )
