from django import template

register = template.Library()


@register.filter
def myfilter(data):
    return data[:3]
