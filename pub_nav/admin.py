from pprint import pprint

from django.contrib import admin
from django.urls import resolve

from .models import Menu, MenuItem


class MenuItemInline(admin.TabularInline):
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
class MenuAdmin(admin.ModelAdmin):
    inlines = (MenuItemInline,)
