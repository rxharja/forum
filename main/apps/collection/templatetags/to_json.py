from django import template
import json

register = template.Library()

@register.simple_tag
def to_json(dic):
    return json.dumps(dic)
