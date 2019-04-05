from django import template
from pub_nav.models import Menu

register = template.Library()


@register.inclusion_tag('nav/nav_menu_items.html', takes_context=True)
def nav_menu_items(context, position):
    menu = Menu.objects.get(position__contains=position)
    context['menu'] = menu
    return context
