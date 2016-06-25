from django.contrib import admin
from .models import Reason


@admin.register(Reason)
class ReasonAdmin(admin.ModelAdmin):
    list_display = ['number', 'get_thumbnail_html', 'name', 'nameFontSize', 'nameLetterSpacing']
    list_display_links = ['number', 'name']
    list_editable = ['nameFontSize', 'nameLetterSpacing']
    ordering = ['number']
