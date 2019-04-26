from django.contrib import admin
from .models import Category, Product, Ingredient
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        fields = ('id', 'meta_title', 'meta_description', 'name', 'content', 'image',)


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product


class IngredientResource(resources.ModelResource):
    class Meta:
        model = Ingredient


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    exclude = ('slug',)
    fieldsets = (
        ('Основное', {
            'classes': ('extrapretty',),
            'fields': ('name', 'content', 'image',)
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description',)
        }),
    )


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_filter = ('category',)
    search_fields = ('name',)
    list_display = ('image_tag', 'name', 'category', 'price')
    list_display_links = ('image_tag', 'name',)
    readonly_fields = ['image_tag']
    exclude = ('slug',)
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
            'fields': ('meta_description',)
        }),
    )
    raw_id_fields = ('category',)


@admin.register(Ingredient)
class IngredientAdmin(ImportExportModelAdmin):
    pass
