from django import template
from django.utils.html import format_html


register = template.Library()


@register.simple_tag
def label_with_info(field, labels_information):
    info_html = ""
    if info_text := labels_information.get(field.name):
        info_html = format_html(
            (
                '<i class="ri-information-line text-info ms-1" '
                'data-bs-toggle="tooltip" '
                'data-bs-html="true" '
                'data-bs-title="{}"></i>'
            ),
            info_text,
        )
    return format_html(
        '<label class="form-label" for="{id_for_label}">{label}{info}</label>',
        id_for_label=field.id_for_label,
        label=field.label,
        info=info_html,
    )
