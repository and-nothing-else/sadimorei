from django.contrib import admin
from .models import Feedback


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['datetime', 'name', 'contact', 'message']
    list_display_links = []


admin.site.register(Feedback, FeedBackAdmin)