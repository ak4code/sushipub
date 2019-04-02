from django import template
from pub_shop.models import Category

register = template.Library()


@register.inclusion_tag('nav/category_menu.html', takes_context=True)
def show_category_menu(context):
    categories = Category.objects.all()
    context['categories'] = categories
    return context
