from django.contrib import admin
from .models import NewsPortal, Publication


@admin.register(NewsPortal, Publication)
class PubAdmin(admin.ModelAdmin):
    pass
