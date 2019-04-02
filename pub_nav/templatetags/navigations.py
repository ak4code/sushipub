from django import template
from pub_nav.models import Menu

register = template.Library()


@register.inclusion_tag('nav/nav_horizontal_menu.html', takes_context=True)
def nav_horizontal_menu(context, position):
    menu = Menu.objects.get(position__contains=position)
    context['menu'] = menu
    return context
