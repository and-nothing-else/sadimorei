from django.contrib import admin
from contact.models import Office


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ["name", "sorting", "lat", "lng", "scale"]
    list_editable = ["lat", "lng", "scale"]
