from django import template

register = template.Library()

# |sub:5
@register.filter
def sub(value, arg):
    return value - arg