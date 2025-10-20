# home/templatetags/string_extras.py
from django import template

register = template.Library()

@register.filter
def split_comma(value):
    """
    Splits a comma-separated string into a list of stripped items.
    Usage: {{ "Django, Python, HTML"|split_comma }}
    """
    if not value:
        return []
    return [item.strip() for item in value.split(',') if item.strip()]