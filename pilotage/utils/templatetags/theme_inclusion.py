"""
https://docs.djangoproject.com/en/dev/howto/custom-template-tags/
"""

from django import template
from django.templatetags.static import static
from django.utils.safestring import mark_safe


"""
This template tags have for goal to mutualize all the dependencies and specifics component from the itou theme.

To use it, you need to copy (if it's not already done) the folder `dist` of https://github.com/betagouv/itou-theme
And you need to paste it into the folder `itou/static/vendor/theme-inclusion`
"""

register = template.Library()

URL_THEME = "vendor/theme-inclusion/"

CSS_DEPENDENCIES_THEME = [
    {
        "is_external": False,
        "src": "stylesheets/app.css",
    },
]


JS_DEPENDENCIES_THEME = [
    {
        "is_external": True,
        "src": "https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js",
        "integrity": "sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r",
    },
    {
        "is_external": True,
        "src": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js",
        "integrity": "sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy",
    },
    {
        "is_external": False,
        "src": "javascripts/app.js",
    },
]


@register.simple_tag
def static_theme(url_path):
    """
    Usage:
        {% load theme_inclusion %}
        {% static_theme url_path %}
    """
    static_path = f"{URL_THEME}{url_path}"
    return static(static_path)


@register.simple_tag
def static_theme_images(url_path):
    """
    Usage:
        {% load theme_inclusion %}
        {% static_theme_images url_path %}
    """
    static_path = f"{URL_THEME}images/{url_path}"
    return static(static_path)


@register.simple_tag
def import_static_css_theme_inclusion():
    scripts_import = ""
    for css_dep in CSS_DEPENDENCIES_THEME:
        if css_dep["is_external"]:
            scripts_import += (
                '<link rel="stylesheet" href="{}" integrity="{}" crossorigin="anonymous" type="text/css">'
            ).format(css_dep["src"], css_dep["integrity"])
        else:
            scripts_import += '<link rel="stylesheet" href="{}" type="text/css">'.format(static_theme(css_dep["src"]))
    return mark_safe(scripts_import)


@register.simple_tag
def import_static_js_theme_inclusion():
    scripts_import = ""
    for js_dep in JS_DEPENDENCIES_THEME:
        if js_dep["is_external"]:
            scripts_import += '<script src="{}" integrity="{}" crossorigin="anonymous"></script>'.format(
                js_dep["src"], js_dep["integrity"]
            )
        else:
            scripts_import += '<script src="{}"></script>'.format(static_theme(js_dep["src"]))
    return mark_safe(scripts_import)
