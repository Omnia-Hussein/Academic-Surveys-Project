from django import template

register = template.Library()


@register.simple_tag(name='divide')
def divide(x, i):
    if int(i) is 0:
        return 0
    return int(x) // int(i)


@register.simple_tag(name='percentage')
def percentage(x, i):
    if int(i) is 0:
        return 0
    return (int(x) * 100) // int(i)
