from django import template
from pub_main.models import Menu

register = template.Library()


@register.simple_tag
def nav_menu_items(position):
    try:
        menu = Menu.objects.prefetch_related('items', 'items__content_object').get(position__contains=position)
        return menu
    except Menu.DoesNotExist as e:
        return ''
