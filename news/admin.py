from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['date', 'name', 'active']
    list_display_links = ['date', 'name']
    list_editable = ['active']
    ordering = ['-date']
