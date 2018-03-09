from django import template

register = template.Library()


@register.filter(name='index')
def index(x, i):
    return x[int(i)]
