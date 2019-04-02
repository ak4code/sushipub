from django.contrib import admin
from .models import Category, Product
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
