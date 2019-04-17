from pprint import pprint

from django.contrib import admin
from .models import Category, Product, Ingredient
from pub_nav.models import MenuItem
from django.contrib.contenttypes.admin import GenericTabularInline


class MenuItemInline(GenericTabularInline):
    model = MenuItem
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [MenuItemInline, ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ('category',)
    search_fields = ('name',)
    list_display = ('image_tag', 'name', 'category', 'price')
    list_display_links = ('image_tag', 'name',)
    readonly_fields = ['image_tag']
    filter_horizontal = ('ingredients',)
    fieldsets = (
        ('Основное', {
            'classes': ('extrapretty',),
            'fields': ('name', 'category', 'price', 'image', 'image_tag', 'quantity', 'weight', 'ingredients')
        }),
        ('Контент', {
            'classes': ('wide',),
            'fields': ('content',)
        }),
        ('Мета', {
            'fields': ('slug', 'meta_description')
        }),
    )


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass
