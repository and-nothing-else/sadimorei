from django.contrib import admin
from .models import *


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['name', 'sorting']
    list_editable = ['sorting']


@admin.register(Doc)
class DocAdmin(admin.ModelAdmin):
    list_display = ['name', 'sorting']
    list_editable = ['sorting']
