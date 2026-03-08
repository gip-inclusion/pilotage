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


@register.simple_tag
def completion_badge(step_information):
    if not step_information.filled:
        extra_classes = "bg-warning-lighter text-warning"
    elif step_information.filled == step_information.total:
        extra_classes = "bg-success-lighter text-success"
    else:
        extra_classes = "bg-info-lighter text-info"
    return format_html(
        '<span class="badge badge-xs {extra_classes} rounded-pill ms-2">{filled}/{total}</span>',
        extra_classes=extra_classes,
        filled=step_information.filled,
        total=step_information.total,
    )
