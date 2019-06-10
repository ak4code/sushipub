from django.contrib import admin
from .models import Category, Product, Ingredient, Destination, Order, OrderItem
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


class ProductVariantInline(admin.TabularInline):
    model = Product
    extra = 1
    verbose_name = "Вариант продукта"
    verbose_name_plural = "Варианты продукта"
    fields = ('name', 'category', 'price', 'image', 'size', 'weight',)


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    inlines = (ProductVariantInline,)
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
            'fields': ('name', 'category', 'price', 'image', 'image_tag', 'size', 'weight', 'text', 'ingredients')
        }),
        ('Контент', {
            'classes': ('collapse',),
            'fields': ('content',)
        }),
        ('Мета', {
            'classes': ('collapse',),
            'fields': ('meta_description',)
        }),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(base=None)


@admin.register(Ingredient)
class IngredientAdmin(ImportExportModelAdmin):
    pass


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    pass


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 2
    readonly_fields = ['amount', ]
    fields = ('product', 'qty', 'amount',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemInline,)
    list_display = ('__str__', 'total',)
