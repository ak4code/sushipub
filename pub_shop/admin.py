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
    list_display = ('image_tag', 'name', 'category', 'price')
    list_display_links = ('name',)
    readonly_fields = ['image_tag']
    filter_horizontal = ('ingredients',)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass
