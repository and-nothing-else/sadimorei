from django.contrib import admin
from sorl.thumbnail.admin import AdminImageMixin
from .models import Photo


@admin.register(Photo)
class PhotoAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ['get_thumbnail_html', 'active', 'name', 'sorting']
    list_display_links = ['name']
    list_editable = ['active', 'sorting']
