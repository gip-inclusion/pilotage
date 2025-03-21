import time

import jwt
from django import template
from django.conf import settings


register = template.Library()


@register.filter()
def iframeurl(value):
    payload = {
        "resource": {"dashboard": value},
        "params": {},
        "exp": round(time.time()) + (60 * 10),
    }

    token = jwt.encode(payload, settings.METABASE_SECRET_KEY, algorithm="HS256")

    return settings.METABASE_BASE_URL + "/embed/dashboard/" + token + "#bordered=true&titled=false"
