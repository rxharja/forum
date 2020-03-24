from django.core.serializers import serialize
from django.template import Library

import json

register = Library()

@register.simple_tag
def jsonify(object):
    return json.dumps(object)
