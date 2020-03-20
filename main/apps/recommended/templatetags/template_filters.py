from django.template import Library

register = Library()


@register.filter
def get_based_on(dictionary, key):
    return dictionary.get(key).get('based_on')
