from django import template
register = template.Library()

@register.filter
def to_currency(value):
    return float(value) / 100.0

@register.simple_tag
def persent(value_1, value_2):
    if value_1 == 0 or value_2 == 0:
        return 0
    else:
        return round(float(value_1 / value_2) * 100, 2)