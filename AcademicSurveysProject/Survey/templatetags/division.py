from django import template

register = template.Library()


@register.simple_tag(name='divide')
def divide(x, i):
    return int(x) // int(i)


@register.simple_tag(name='percentage')
def percentage(x, i):
    return (int(x) * 100) // int(i)
