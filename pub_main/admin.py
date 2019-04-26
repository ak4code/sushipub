from django.contrib import admin
from .models import Shop, Phone, Link, Page, Menu, MenuItem
from solo.admin import SingletonModelAdmin
from django.urls import resolve
from genericadmin.admin import GenericAdminModelAdmin, TabularInlineWithGeneric


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
    fieldsets = (
        ('Основное', {
            'classes': ('extrapretty',),
            'fields': ('title', 'content',)
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'slug',)
        }),
    )


class MenuItemInline(TabularInlineWithGeneric):
    model = MenuItem
    extra = 1

    def get_parent_object_from_request(self, request):

        resolved = resolve(request.path_info)
        if resolved.kwargs:
            return self.parent_model.objects.get(pk=resolved.kwargs['object_id'])
        return None

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "parent":
            kwargs["queryset"] = self.get_queryset(request).filter(menu=self.get_parent_object_from_request(request))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Menu)
class MenuAdmin(GenericAdminModelAdmin):
    inlines = (MenuItemInline,)
