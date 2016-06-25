from django.contrib import admin
from .models import PressRelease


@admin.register(PressRelease)
class PressReleaseAdmin(admin.ModelAdmin):
    list_display = ['date', 'name']
    list_display_links = ['date', 'name']
    ordering = ['-date']
