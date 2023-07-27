from django import template

register = template.Library()

@register.filter(name='intcomma')
def intcomma_filter(value):
    if value is None:
        return ''
    try:
        int_value = int(value)
        return "{:,}".format(int_value)
    except (ValueError, TypeError):
        return value