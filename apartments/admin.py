from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from .models import *
from sorl.thumbnail.admin import AdminImageMixin


class BuildingPhotoInline(AdminImageMixin, admin.TabularInline):
    model = BuildingPhoto
    extra = 8
    # template = "admin/edit_inline/table.html"


class BuildingAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ['name', 'code', 'sorting']
    list_display_links = ['code', 'name']
    list_editable = ['sorting']
    fieldsets = [
        (None, {
            'fields': ('name', 'code', 'sorting')
        }),
        (_('Description'), {
            'fields': ('description_title', 'description', 'photo')
        })
    ]
    inlines = [BuildingPhotoInline]


class LayoutTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'sorting']
    list_editable = ['sorting']


class LayoutAdmin(admin.ModelAdmin):
    list_display = ['name']


class PlacementAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']


class ApartmentAdmin(admin.ModelAdmin):
    list_display = ['code', 'status', 'square', 'layout_type', 'price']
    list_editable = ['status', 'price']
    list_display_links = ['code', 'square', 'layout_type']
    list_filter = ['building', 'status', 'layout_type', 'floor', 'mansard', 'sea_view', 'terrace', 'lawn']
    search_fields = ['code']
    fieldsets = [
        (None, {
            'fields': ('code', 'building'),
            'classes': ['wide']
        }),
        (_('Floor'), {
            'fields': ('floor', 'mansard'),
            'classes': ['wide']
        }),
        (_('Square'), {
            'fields': ('square', 'balcony_square', 'loggia_square'),
            'classes': ['wide']
        }),
        (_('Layout'), {
            'fields': ('layout_type', 'layout', 'placement'),
            'classes': ['wide']
        }),
        (_('Benefits'), {
            'fields': ('sea_view', 'terrace', 'lawn'),
            'classes': ['wide']
        }),
        (_('Sale'), {
            'fields': ('price', 'status'),
            'classes': ['wide']
        })
    ]


admin.site.register(Building, BuildingAdmin)
admin.site.register(LayoutType, LayoutTypeAdmin)
admin.site.register(Layout, LayoutAdmin)
admin.site.register(Placement, PlacementAdmin)
admin.site.register(ApartmentDescription)
admin.site.register(Apartment, ApartmentAdmin)
