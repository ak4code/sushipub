from django import template
from pub_main.models import Menu

register = template.Library()


@register.inclusion_tag('nav/nav_menu_items.html', takes_context=True)
def nav_menu_items(context, position):
    context['no_menu'] = False
    try:
        menu = Menu.objects.get(position__contains=position)
        context['menu'] = menu
    except Menu.DoesNotExist as e:
        context['error'] = e
        context['no_menu'] = True
    return context
