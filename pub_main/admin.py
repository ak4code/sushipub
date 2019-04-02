from django.contrib import admin
from .models import Shop, Phone, Link, Page
from solo.admin import SingletonModelAdmin


class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 1


class LinkInline(admin.TabularInline):
    model = Link
    extra = 1


@admin.register(Shop)
class ShopAdmin(SingletonModelAdmin):
    inlines = [
        PhoneInline,
        LinkInline
    ]


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')
    prepopulated_fields = {"slug": ("title",)}

# shop = Shop.get_solo()
