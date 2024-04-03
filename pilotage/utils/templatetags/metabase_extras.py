from django.conf import settings
from django import template

import jwt
import time

register = template.Library()


@register.filter()
def iframeurl(value):
    payload = {
        "resource": {"dashboard": value},
        "params": {},
        "exp": round(time.time()) + (60 * 10),
    }

    token = jwt.encode(payload, settings.METABASE_SECRET_KEY, algorithm="HS256")

    return (
        "http://stats.inclusion.beta.gouv.fr"
        + "/embed/dashboard/"
        + token
        + "#bordered=true&titled=true"
    )
